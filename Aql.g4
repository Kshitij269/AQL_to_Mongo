grammar Aql;

query
    : selectClause fromClause whereClause? SEMI
    ;

selectClause
    : SELECT selectExpr (COMMA selectExpr)*
    ;

selectExpr
    : path (AS ID)?
    ;

fromClause
    : FROM path ID (CONTAINS path ID (LBRACK ID RBRACK)?)*
    ;

whereClause
    : WHERE expression
    ;

expression
    : condition (logicalOp condition)*
    ;

condition
    : path comparator value
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

// Types
ID          : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING      : '\'' (~['\\] | '\\' .)* '\'' ;
NUMBER      : [0-9]+ ('.' [0-9]+)? ;
BOOLEAN     : 'true' | 'false' ;

// Ignore whitespace
WS          : [ \t\r\n]+ -> skip ;
