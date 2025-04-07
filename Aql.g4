grammar Aql;

query       : selectClause fromClause whereClause? SEMI ;
selectClause: SELECT selectExpr (COMMA selectExpr)* ;
selectExpr  : path (AS ID)? ;
fromClause  : FROM path ID (CONTAINS path ID)* ;
whereClause : WHERE condition ;
condition   : path EQUALS STRING ;

path        : pathPart (SLASH pathPart)* ;
pathPart    : ID (LBRACK ID RBRACK)? ;

SELECT      : 'SELECT';
FROM        : 'FROM';
CONTAINS    : 'CONTAINS';
WHERE       : 'WHERE';
AS          : 'AS';
EQUALS      : '=';
SEMI        : ';';
COMMA       : ',';
SLASH       : '/';
LBRACK      : '[';
RBRACK      : ']';
ID          : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING      : '\'' (~['\\] | '\\' .)* '\'' ;
WS          : [ \t\r\n]+ -> skip ;
