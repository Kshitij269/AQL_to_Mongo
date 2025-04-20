# Generated from Aql.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,98,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,3,0,28,
        8,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,1,2,1,2,
        1,2,3,2,44,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,55,8,3,5,
        3,57,8,3,10,3,12,3,60,9,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,69,8,5,
        10,5,12,5,72,9,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,
        10,1,10,5,10,87,8,10,10,10,12,10,90,9,10,1,11,1,11,1,11,1,11,3,11,
        96,8,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,3,1,0,8,13,
        1,0,6,7,1,0,20,22,93,0,24,1,0,0,0,2,31,1,0,0,0,4,40,1,0,0,0,6,45,
        1,0,0,0,8,61,1,0,0,0,10,64,1,0,0,0,12,73,1,0,0,0,14,77,1,0,0,0,16,
        79,1,0,0,0,18,81,1,0,0,0,20,83,1,0,0,0,22,91,1,0,0,0,24,25,3,2,1,
        0,25,27,3,6,3,0,26,28,3,8,4,0,27,26,1,0,0,0,27,28,1,0,0,0,28,29,
        1,0,0,0,29,30,5,14,0,0,30,1,1,0,0,0,31,32,5,1,0,0,32,37,3,4,2,0,
        33,34,5,15,0,0,34,36,3,4,2,0,35,33,1,0,0,0,36,39,1,0,0,0,37,35,1,
        0,0,0,37,38,1,0,0,0,38,3,1,0,0,0,39,37,1,0,0,0,40,43,3,20,10,0,41,
        42,5,5,0,0,42,44,5,19,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,5,1,0,0,
        0,45,46,5,2,0,0,46,47,3,20,10,0,47,58,5,19,0,0,48,49,5,3,0,0,49,
        50,3,20,10,0,50,54,5,19,0,0,51,52,5,17,0,0,52,53,5,19,0,0,53,55,
        5,18,0,0,54,51,1,0,0,0,54,55,1,0,0,0,55,57,1,0,0,0,56,48,1,0,0,0,
        57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,7,1,0,0,0,60,58,1,0,
        0,0,61,62,5,4,0,0,62,63,3,10,5,0,63,9,1,0,0,0,64,70,3,12,6,0,65,
        66,3,16,8,0,66,67,3,12,6,0,67,69,1,0,0,0,68,65,1,0,0,0,69,72,1,0,
        0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,11,1,0,0,0,72,70,1,0,0,0,73,74,
        3,20,10,0,74,75,3,14,7,0,75,76,3,18,9,0,76,13,1,0,0,0,77,78,7,0,
        0,0,78,15,1,0,0,0,79,80,7,1,0,0,80,17,1,0,0,0,81,82,7,2,0,0,82,19,
        1,0,0,0,83,88,3,22,11,0,84,85,5,16,0,0,85,87,3,22,11,0,86,84,1,0,
        0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,21,1,0,0,0,90,88,
        1,0,0,0,91,95,5,19,0,0,92,93,5,17,0,0,93,94,5,19,0,0,94,96,5,18,
        0,0,95,92,1,0,0,0,95,96,1,0,0,0,96,23,1,0,0,0,8,27,37,43,54,58,70,
        88,95
    ]

class AqlParser ( Parser ):

    grammarFileName = "Aql.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SELECT'", "'FROM'", "'CONTAINS'", "'WHERE'", 
                     "'AS'", "'AND'", "'OR'", "'='", "'!='", "'>'", "'<'", 
                     "'>='", "'<='", "';'", "','", "'/'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "CONTAINS", "WHERE", 
                      "AS", "AND", "OR", "EQUALS", "NOT_EQUALS", "GT", "LT", 
                      "GTE", "LTE", "SEMI", "COMMA", "SLASH", "LBRACK", 
                      "RBRACK", "ID", "STRING", "NUMBER", "BOOLEAN", "WS" ]

    RULE_query = 0
    RULE_selectClause = 1
    RULE_selectExpr = 2
    RULE_fromClause = 3
    RULE_whereClause = 4
    RULE_expression = 5
    RULE_condition = 6
    RULE_comparator = 7
    RULE_logicalOp = 8
    RULE_value = 9
    RULE_path = 10
    RULE_pathPart = 11

    ruleNames =  [ "query", "selectClause", "selectExpr", "fromClause", 
                   "whereClause", "expression", "condition", "comparator", 
                   "logicalOp", "value", "path", "pathPart" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    CONTAINS=3
    WHERE=4
    AS=5
    AND=6
    OR=7
    EQUALS=8
    NOT_EQUALS=9
    GT=10
    LT=11
    GTE=12
    LTE=13
    SEMI=14
    COMMA=15
    SLASH=16
    LBRACK=17
    RBRACK=18
    ID=19
    STRING=20
    NUMBER=21
    BOOLEAN=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectClause(self):
            return self.getTypedRuleContext(AqlParser.SelectClauseContext,0)


        def fromClause(self):
            return self.getTypedRuleContext(AqlParser.FromClauseContext,0)


        def SEMI(self):
            return self.getToken(AqlParser.SEMI, 0)

        def whereClause(self):
            return self.getTypedRuleContext(AqlParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return AqlParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = AqlParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.selectClause()
            self.state = 25
            self.fromClause()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 26
                self.whereClause()


            self.state = 29
            self.match(AqlParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(AqlParser.SELECT, 0)

        def selectExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AqlParser.SelectExprContext)
            else:
                return self.getTypedRuleContext(AqlParser.SelectExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AqlParser.COMMA)
            else:
                return self.getToken(AqlParser.COMMA, i)

        def getRuleIndex(self):
            return AqlParser.RULE_selectClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectClause" ):
                listener.enterSelectClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectClause" ):
                listener.exitSelectClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectClause" ):
                return visitor.visitSelectClause(self)
            else:
                return visitor.visitChildren(self)




    def selectClause(self):

        localctx = AqlParser.SelectClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_selectClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(AqlParser.SELECT)
            self.state = 32
            self.selectExpr()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 33
                self.match(AqlParser.COMMA)
                self.state = 34
                self.selectExpr()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def path(self):
            return self.getTypedRuleContext(AqlParser.PathContext,0)


        def AS(self):
            return self.getToken(AqlParser.AS, 0)

        def ID(self):
            return self.getToken(AqlParser.ID, 0)

        def getRuleIndex(self):
            return AqlParser.RULE_selectExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectExpr" ):
                listener.enterSelectExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectExpr" ):
                listener.exitSelectExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectExpr" ):
                return visitor.visitSelectExpr(self)
            else:
                return visitor.visitChildren(self)




    def selectExpr(self):

        localctx = AqlParser.SelectExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_selectExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.path()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 41
                self.match(AqlParser.AS)
                self.state = 42
                self.match(AqlParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FromClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(AqlParser.FROM, 0)

        def path(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AqlParser.PathContext)
            else:
                return self.getTypedRuleContext(AqlParser.PathContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AqlParser.ID)
            else:
                return self.getToken(AqlParser.ID, i)

        def CONTAINS(self, i:int=None):
            if i is None:
                return self.getTokens(AqlParser.CONTAINS)
            else:
                return self.getToken(AqlParser.CONTAINS, i)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(AqlParser.LBRACK)
            else:
                return self.getToken(AqlParser.LBRACK, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(AqlParser.RBRACK)
            else:
                return self.getToken(AqlParser.RBRACK, i)

        def getRuleIndex(self):
            return AqlParser.RULE_fromClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFromClause" ):
                listener.enterFromClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFromClause" ):
                listener.exitFromClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFromClause" ):
                return visitor.visitFromClause(self)
            else:
                return visitor.visitChildren(self)




    def fromClause(self):

        localctx = AqlParser.FromClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fromClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(AqlParser.FROM)
            self.state = 46
            self.path()
            self.state = 47
            self.match(AqlParser.ID)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 48
                self.match(AqlParser.CONTAINS)
                self.state = 49
                self.path()
                self.state = 50
                self.match(AqlParser.ID)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 51
                    self.match(AqlParser.LBRACK)
                    self.state = 52
                    self.match(AqlParser.ID)
                    self.state = 53
                    self.match(AqlParser.RBRACK)


                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(AqlParser.WHERE, 0)

        def expression(self):
            return self.getTypedRuleContext(AqlParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AqlParser.RULE_whereClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClause" ):
                listener.enterWhereClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClause" ):
                listener.exitWhereClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhereClause" ):
                return visitor.visitWhereClause(self)
            else:
                return visitor.visitChildren(self)




    def whereClause(self):

        localctx = AqlParser.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(AqlParser.WHERE)
            self.state = 62
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AqlParser.ConditionContext)
            else:
                return self.getTypedRuleContext(AqlParser.ConditionContext,i)


        def logicalOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AqlParser.LogicalOpContext)
            else:
                return self.getTypedRuleContext(AqlParser.LogicalOpContext,i)


        def getRuleIndex(self):
            return AqlParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = AqlParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.condition()
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 65
                self.logicalOp()
                self.state = 66
                self.condition()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def path(self):
            return self.getTypedRuleContext(AqlParser.PathContext,0)


        def comparator(self):
            return self.getTypedRuleContext(AqlParser.ComparatorContext,0)


        def value(self):
            return self.getTypedRuleContext(AqlParser.ValueContext,0)


        def getRuleIndex(self):
            return AqlParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = AqlParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.path()
            self.state = 74
            self.comparator()
            self.state = 75
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(AqlParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(AqlParser.NOT_EQUALS, 0)

        def GT(self):
            return self.getToken(AqlParser.GT, 0)

        def LT(self):
            return self.getToken(AqlParser.LT, 0)

        def GTE(self):
            return self.getToken(AqlParser.GTE, 0)

        def LTE(self):
            return self.getToken(AqlParser.LTE, 0)

        def getRuleIndex(self):
            return AqlParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = AqlParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(AqlParser.AND, 0)

        def OR(self):
            return self.getToken(AqlParser.OR, 0)

        def getRuleIndex(self):
            return AqlParser.RULE_logicalOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOp" ):
                listener.enterLogicalOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOp" ):
                listener.exitLogicalOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOp" ):
                return visitor.visitLogicalOp(self)
            else:
                return visitor.visitChildren(self)




    def logicalOp(self):

        localctx = AqlParser.LogicalOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_logicalOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AqlParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(AqlParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(AqlParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return AqlParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = AqlParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pathPart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AqlParser.PathPartContext)
            else:
                return self.getTypedRuleContext(AqlParser.PathPartContext,i)


        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(AqlParser.SLASH)
            else:
                return self.getToken(AqlParser.SLASH, i)

        def getRuleIndex(self):
            return AqlParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPath" ):
                return visitor.visitPath(self)
            else:
                return visitor.visitChildren(self)




    def path(self):

        localctx = AqlParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_path)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.pathPart()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 84
                self.match(AqlParser.SLASH)
                self.state = 85
                self.pathPart()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AqlParser.ID)
            else:
                return self.getToken(AqlParser.ID, i)

        def LBRACK(self):
            return self.getToken(AqlParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(AqlParser.RBRACK, 0)

        def getRuleIndex(self):
            return AqlParser.RULE_pathPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathPart" ):
                listener.enterPathPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathPart" ):
                listener.exitPathPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPathPart" ):
                return visitor.visitPathPart(self)
            else:
                return visitor.visitChildren(self)




    def pathPart(self):

        localctx = AqlParser.PathPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_pathPart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(AqlParser.ID)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 92
                self.match(AqlParser.LBRACK)
                self.state = 93
                self.match(AqlParser.ID)
                self.state = 94
                self.match(AqlParser.RBRACK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





