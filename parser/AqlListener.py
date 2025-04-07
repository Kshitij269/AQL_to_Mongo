# Generated from Aql.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AqlParser import AqlParser
else:
    from AqlParser import AqlParser

# This class defines a complete listener for a parse tree produced by AqlParser.
class AqlListener(ParseTreeListener):

    # Enter a parse tree produced by AqlParser#query.
    def enterQuery(self, ctx:AqlParser.QueryContext):
        pass

    # Exit a parse tree produced by AqlParser#query.
    def exitQuery(self, ctx:AqlParser.QueryContext):
        pass


    # Enter a parse tree produced by AqlParser#selectClause.
    def enterSelectClause(self, ctx:AqlParser.SelectClauseContext):
        pass

    # Exit a parse tree produced by AqlParser#selectClause.
    def exitSelectClause(self, ctx:AqlParser.SelectClauseContext):
        pass


    # Enter a parse tree produced by AqlParser#selectExpr.
    def enterSelectExpr(self, ctx:AqlParser.SelectExprContext):
        pass

    # Exit a parse tree produced by AqlParser#selectExpr.
    def exitSelectExpr(self, ctx:AqlParser.SelectExprContext):
        pass


    # Enter a parse tree produced by AqlParser#fromClause.
    def enterFromClause(self, ctx:AqlParser.FromClauseContext):
        pass

    # Exit a parse tree produced by AqlParser#fromClause.
    def exitFromClause(self, ctx:AqlParser.FromClauseContext):
        pass


    # Enter a parse tree produced by AqlParser#whereClause.
    def enterWhereClause(self, ctx:AqlParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by AqlParser#whereClause.
    def exitWhereClause(self, ctx:AqlParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by AqlParser#condition.
    def enterCondition(self, ctx:AqlParser.ConditionContext):
        pass

    # Exit a parse tree produced by AqlParser#condition.
    def exitCondition(self, ctx:AqlParser.ConditionContext):
        pass


    # Enter a parse tree produced by AqlParser#path.
    def enterPath(self, ctx:AqlParser.PathContext):
        pass

    # Exit a parse tree produced by AqlParser#path.
    def exitPath(self, ctx:AqlParser.PathContext):
        pass


    # Enter a parse tree produced by AqlParser#pathPart.
    def enterPathPart(self, ctx:AqlParser.PathPartContext):
        pass

    # Exit a parse tree produced by AqlParser#pathPart.
    def exitPathPart(self, ctx:AqlParser.PathPartContext):
        pass



del AqlParser