# Generated from Aql.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AqlParser import AqlParser
else:
    from AqlParser import AqlParser

# This class defines a complete generic visitor for a parse tree produced by AqlParser.

class AqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AqlParser#query.
    def visitQuery(self, ctx:AqlParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#selectClause.
    def visitSelectClause(self, ctx:AqlParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#selectExpr.
    def visitSelectExpr(self, ctx:AqlParser.SelectExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#fromClause.
    def visitFromClause(self, ctx:AqlParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#whereClause.
    def visitWhereClause(self, ctx:AqlParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#expression.
    def visitExpression(self, ctx:AqlParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#simpleExpr.
    def visitSimpleExpr(self, ctx:AqlParser.SimpleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#comparator.
    def visitComparator(self, ctx:AqlParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#logicalOp.
    def visitLogicalOp(self, ctx:AqlParser.LogicalOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#orderByClause.
    def visitOrderByClause(self, ctx:AqlParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#orderField.
    def visitOrderField(self, ctx:AqlParser.OrderFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#value.
    def visitValue(self, ctx:AqlParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#path.
    def visitPath(self, ctx:AqlParser.PathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#pathPart.
    def visitPathPart(self, ctx:AqlParser.PathPartContext):
        return self.visitChildren(ctx)



del AqlParser