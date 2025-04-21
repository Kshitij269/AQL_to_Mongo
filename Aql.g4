grammar Aql;

query
    : selectClause fromClause whereClause? orderByClause? SEMI
    ;

selectClause
    : SELECT selectExpr (COMMA selectExpr)*
    ;

selectExpr
    : path (AS ID)?
    ;

fromClause
    : FROM path ID (CONTAINS path ID (LBRACK ID RBRACK)? )*
    ;

whereClause
    : WHERE expression
    ;

expression
    : NOT? simpleExpr (logicalOp NOT? simpleExpr)*
    ;

simpleExpr
    : LPAREN expression RPAREN
    | path comparator value
    | path MATCHES STRING
    | path EXISTS
    ;

comparator
    : EQUALS
    | NOT_EQUALS
    | GT
    | LT
    | GTE
    | LTE
    ;

logicalOp
    : AND
    | OR
    ;

orderByClause
    : ORDER BY orderField (COMMA orderField)*
    ;

orderField
    : path (ASC | DESC)?
    ;

value
    : STRING
    | NUMBER
    | BOOLEAN
    ;

path
    : pathPart (SLASH pathPart)*
    ;

pathPart
    : ID (LBRACK ID RBRACK)?
    ;

// Keywords
SELECT      : 'SELECT';
FROM        : 'FROM';
CONTAINS    : 'CONTAINS';
WHERE       : 'WHERE';
AS          : 'AS';
AND         : 'AND';
OR          : 'OR';
NOT         : 'NOT';
MATCHES     : 'MATCHES';
EXISTS      : 'EXISTS';
ORDER       : 'ORDER';
BY          : 'BY';
ASC         : 'ASC';
DESC        : 'DESC';

// Operators
EQUALS      : '=';
NOT_EQUALS  : '!=';
GT          : '>';
LT          : '<';
GTE         : '>=';
LTE         : '<=';

// Symbols
SEMI        : ';';
COMMA       : ',';
SLASH       : '/';
LBRACK      : '[';
RBRACK      : ']';
LPAREN      : '(';
RPAREN      : ')';

// Types
ID          : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING      : '\'' (~['\\] | '\\' .)* '\'' ;
NUMBER      : [0-9]+ ('.' [0-9]+)? ;
BOOLEAN     : 'true' | 'false' ;

// Ignore whitespace
WS          : [ \t\r\n]+ -> skip ;
