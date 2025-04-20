from AqlLexer import AqlLexer
from AqlParser import AqlParser
from AqlVisitor import AqlVisitor
from antlr4 import *

class AqlToMongoVisitor(AqlVisitor):
    def __init__(self):
        self.select_fields = []
        self.collection = None
        self.where_clause = {}

    def visitQuery(self, ctx):
        self.visit(ctx.selectClause())
        self.visit(ctx.fromClause())
        if ctx.whereClause():
            self.where_clause = self.visit(ctx.whereClause())
        return self.build_query()

    def visitSelectClause(self, ctx):
        for expr in ctx.selectExpr():
            self.select_fields.append(self.visit(expr))

    def visitSelectExpr(self, ctx):
        path = self.flatten_path(ctx.path())
        alias = ctx.ID()
        return {"field": path, "alias": alias.getText() if alias else path}

    def visitFromClause(self, ctx):
        self.collection = ctx.ID(0).getText()

    def visitWhereClause(self, ctx):
        return self.visit(ctx.expression())

    def visitExpression(self, ctx):
        if len(ctx.condition()) == 1:
            return self.visit(ctx.condition(0))

        conditions = [self.visit(ctx.condition(i)) for i in range(len(ctx.condition()))]
        operators = [ctx.logicalOp(i).getText().lower() for i in range(len(ctx.logicalOp()))]

        result = conditions[0]
        for i, op in enumerate(operators):
            if op == 'and':
                result = {"$and": [result, conditions[i + 1]]}
            elif op == 'or':
                result = {"$or": [result, conditions[i + 1]]}
        return result

    def visitCondition(self, ctx):
        field = self.flatten_path(ctx.path())
        value_ctx = ctx.value()

        # Only append suffix if it's not already a terminal field
        if not field.endswith(("value", "magnitude", "code_string", "originalText")):
            if value_ctx.STRING() or value_ctx.BOOLEAN():
                field += ".value"
            elif value_ctx.NUMBER():
                field += ".magnitude"

        if value_ctx.STRING():
            value = value_ctx.STRING().getText().strip("'")
        elif value_ctx.NUMBER():
            num_text = value_ctx.NUMBER().getText()
            value = float(num_text) if '.' in num_text else int(num_text)
        elif value_ctx.BOOLEAN():
            value = value_ctx.BOOLEAN().getText().lower() == 'true'
        else:
            value = None

        comp = ctx.comparator().getText()
        if comp == '=':
            return {field: value}
        elif comp == '!=':
            return {field: {"$ne": value}}
        elif comp == '>':
            return {field: {"$gt": value}}
        elif comp == '<':
            return {field: {"$lt": value}}
        elif comp == '>=':
            return {field: {"$gte": value}}
        elif comp == '<=':
            return {field: {"$lte": value}}
        else:
            return {field: value}

    def flatten_path(self, ctx):
        parts = []
        for part_ctx in ctx.pathPart():
            base = part_ctx.ID(0).getText()
            if part_ctx.LBRACK():
                sub = part_ctx.ID(1).getText()
                parts.append(f"{base}.parts.{sub}")
            else:
                parts.append(base)
        return '.'.join(parts)

    def build_query(self):
        projection = {field["field"]: 1 for field in self.select_fields}
        aliases = {field["alias"]: field["field"] for field in self.select_fields}
        return {
            "collection": self.collection,
            "projection": projection,
            "filter": self.where_clause,
            "aliases": aliases
        }

def parse_aql(aql_query):
    input_stream = InputStream(aql_query)
    lexer = AqlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AqlParser(stream)
    parser.removeErrorListeners()
    parser._errHandler = BailErrorStrategy()  # Avoid silent parse failures
    tree = parser.query()

    visitor = AqlToMongoVisitor()
    return visitor.visit(tree)