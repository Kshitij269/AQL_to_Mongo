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
            self.visit(ctx.whereClause())
        return self.build_query()

    def visitSelectClause(self, ctx):
        for expr in ctx.selectExpr():
            field = self.visit(expr)
            self.select_fields.append(field)

    def visitSelectExpr(self, ctx):
        path = self.flatten_path(ctx.path())
        alias = ctx.ID()
        return { "field": path, "alias": alias.getText() if alias else path }

    def visitFromClause(self, ctx):
        self.collection = ctx.ID(0).getText()  # Usually after FROM

    def visitWhereClause(self, ctx):
        cond = ctx.condition()
        field = self.flatten_path(cond.path())
        value = cond.STRING().getText().strip("'")
        self.where_clause[field] = value

    def flatten_path(self, ctx):
        parts = []
        for part in ctx.getChildren():
            if isinstance(part, AqlParser.PathPartContext):
                key = part.ID(0).getText()
                if part.LBRACK():
                    bracket_key = part.ID(1).getText()
                    parts.append(f"{key}.parts.{bracket_key}")
                else:
                    parts.append(key)
        # Always end with '.value' if field (you can make this conditional if needed)
        if not parts[-1].endswith('value'):
            parts.append("value")
        return '.'.join(parts)

    def build_query(self):
        projection = {f["field"]: 1 for f in self.select_fields}
        aliases = {f["alias"]: f["field"] for f in self.select_fields}
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
    tree = parser.query()

    visitor = AqlToMongoVisitor()
    return visitor.visit(tree)
