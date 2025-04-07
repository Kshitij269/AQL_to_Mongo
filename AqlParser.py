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
        4,1,14,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,3,0,20,8,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,28,
        8,1,10,1,12,1,31,9,1,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,5,3,45,8,3,10,3,12,3,48,9,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,5,6,60,8,6,10,6,12,6,63,9,6,1,7,1,7,1,7,1,7,3,7,69,8,
        7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,0,68,0,16,1,0,0,0,2,23,1,0,0,0,
        4,32,1,0,0,0,6,37,1,0,0,0,8,49,1,0,0,0,10,52,1,0,0,0,12,56,1,0,0,
        0,14,64,1,0,0,0,16,17,3,2,1,0,17,19,3,6,3,0,18,20,3,8,4,0,19,18,
        1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,7,0,0,22,1,1,0,0,0,23,
        24,5,1,0,0,24,29,3,4,2,0,25,26,5,8,0,0,26,28,3,4,2,0,27,25,1,0,0,
        0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,3,1,0,0,0,31,29,1,
        0,0,0,32,35,3,12,6,0,33,34,5,5,0,0,34,36,5,12,0,0,35,33,1,0,0,0,
        35,36,1,0,0,0,36,5,1,0,0,0,37,38,5,2,0,0,38,39,3,12,6,0,39,46,5,
        12,0,0,40,41,5,3,0,0,41,42,3,12,6,0,42,43,5,12,0,0,43,45,1,0,0,0,
        44,40,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,7,1,0,
        0,0,48,46,1,0,0,0,49,50,5,4,0,0,50,51,3,10,5,0,51,9,1,0,0,0,52,53,
        3,12,6,0,53,54,5,6,0,0,54,55,5,13,0,0,55,11,1,0,0,0,56,61,3,14,7,
        0,57,58,5,9,0,0,58,60,3,14,7,0,59,57,1,0,0,0,60,63,1,0,0,0,61,59,
        1,0,0,0,61,62,1,0,0,0,62,13,1,0,0,0,63,61,1,0,0,0,64,68,5,12,0,0,
        65,66,5,10,0,0,66,67,5,12,0,0,67,69,5,11,0,0,68,65,1,0,0,0,68,69,
        1,0,0,0,69,15,1,0,0,0,6,19,29,35,46,61,68
    ]

class AqlParser ( Parser ):

    grammarFileName = "Aql.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SELECT'", "'FROM'", "'CONTAINS'", "'WHERE'", 
                     "'AS'", "'='", "';'", "','", "'/'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "CONTAINS", "WHERE", 
                      "AS", "EQUALS", "SEMI", "COMMA", "SLASH", "LBRACK", 
                      "RBRACK", "ID", "STRING", "WS" ]

    RULE_query = 0
    RULE_selectClause = 1
    RULE_selectExpr = 2
    RULE_fromClause = 3
    RULE_whereClause = 4
    RULE_condition = 5
    RULE_path = 6
    RULE_pathPart = 7

    ruleNames =  [ "query", "selectClause", "selectExpr", "fromClause", 
                   "whereClause", "condition", "path", "pathPart" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    CONTAINS=3
    WHERE=4
    AS=5
    EQUALS=6
    SEMI=7
    COMMA=8
    SLASH=9
    LBRACK=10
    RBRACK=11
    ID=12
    STRING=13
    WS=14

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
            self.state = 16
            self.selectClause()
            self.state = 17
            self.fromClause()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 18
                self.whereClause()


            self.state = 21
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
            self.state = 23
            self.match(AqlParser.SELECT)
            self.state = 24
            self.selectExpr()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 25
                self.match(AqlParser.COMMA)
                self.state = 26
                self.selectExpr()
                self.state = 31
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
            self.state = 32
            self.path()
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 33
                self.match(AqlParser.AS)
                self.state = 34
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
            self.state = 37
            self.match(AqlParser.FROM)
            self.state = 38
            self.path()
            self.state = 39
            self.match(AqlParser.ID)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 40
                self.match(AqlParser.CONTAINS)
                self.state = 41
                self.path()
                self.state = 42
                self.match(AqlParser.ID)
                self.state = 48
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

        def condition(self):
            return self.getTypedRuleContext(AqlParser.ConditionContext,0)


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
            self.state = 49
            self.match(AqlParser.WHERE)
            self.state = 50
            self.condition()
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


        def EQUALS(self):
            return self.getToken(AqlParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(AqlParser.STRING, 0)

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
        self.enterRule(localctx, 10, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.path()
            self.state = 53
            self.match(AqlParser.EQUALS)
            self.state = 54
            self.match(AqlParser.STRING)
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
        self.enterRule(localctx, 12, self.RULE_path)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.pathPart()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 57
                self.match(AqlParser.SLASH)
                self.state = 58
                self.pathPart()
                self.state = 63
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
        self.enterRule(localctx, 14, self.RULE_pathPart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(AqlParser.ID)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 65
                self.match(AqlParser.LBRACK)
                self.state = 66
                self.match(AqlParser.ID)
                self.state = 67
                self.match(AqlParser.RBRACK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





