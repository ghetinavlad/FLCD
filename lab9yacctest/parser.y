%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int yylex();
void yyerror(char *s);

#define YYDEBUG 1
%}

%token IDENTIFIER
%token CONSTANT
%token START
%token EXIT
%token IF
%token ELSE
%token FOR
%token WHILE
%token READ
%token WRITE
%token INT
%token STRING
%token CONST
%token ARRAY
%token COLON
%token SEMI_COLON
%token COMA
%token DOT
%token LEFT_ROUND_PARENTHESIS
%token RIGHT_ROUND_PARENTHESIS
%token LEFT_SQUARE_PARENTHESIS
%token RIGHT_SQUARE_PARENTHESIS
%token LEFT_BRACKET
%token RIGHT_BRACKET
%token PLUS
%token MINUS
%token MULTIPLY
%token DIVISION
%token MODULO
%token LESS_THAN
%token GREATER_THAN
%token LESS_OR_EQUAL_THAN
%token GREATER_OR_EQUAL_THAN
%token DIFFERENT
%token ASSIGNMENT
%token EQUAL

%start program

%%

program : START stmtlist EXIT ;
type1 : INT ;
type1 : STRING ;
type : type1 ;
type : arraydecl ;
stmtlist : stmt stmtlist ; 
stmtlist : stmt ;
stmt : simplestmt SEMI_COLON ;
stmt : structstmt ;
simplestmt : declaration ;
simplestmt : assignstmt ;
simplestmt : iostmt ; 
structstmt : ifstmt ; 
structstmt : forstmt ; 
structstmt : whilestmt ;
declaration : type IDENTIFIER ;
arraydecl : type1 ARRAY LEFT_SQUARE_PARENTHESIS INT RIGHT_SQUARE_PARENTHESIS ;
assignstmt : IDENTIFIER ASSIGNMENT expression ; 
iostmt : READ LEFT_ROUND_PARENTHESIS IDENTIFIER RIGHT_ROUND_PARENTHESIS ;
iostmt : WRITE LEFT_ROUND_PARENTHESIS IDENTIFIER RIGHT_ROUND_PARENTHESIS ;
ifstmt : IF LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS LEFT_BRACKET stmtlist RIGHT_BRACKET ;
ifstmt : IF LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS LEFT_BRACKET stmtlist RIGHT_BRACKET ELSE LEFT_BRACKET stmtlist RIGHT_BRACKET ;
forstmt : FOR LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS LEFT_BRACKET stmtlist RIGHT_BRACKET ;
whilestmt : WHILE LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS LEFT_BRACKET stmtlist RIGHT_BRACKET ;
expression : term operation expression ;
expression : term ;
condition : expression relation expression ;
operation : PLUS
		| MINUS
		| MULTIPLY
		| DIVISION
		| MODULO ;
term : IDENTIFIER ;
term : CONSTANT ;
relation : LESS_THAN
		| GREATER_THAN
		| LESS_OR_EQUAL_THAN
		| GREATER_OR_EQUAL_THAN
		| DIFFERENT
		| EQUAL ;

%%

void yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

int main(int argc, char **argv)
{
  if (argc > 1)
    yyin = fopen(argv[1], "r");
  if ( (argc > 2) && ( !strcmp(argv[2], "-d") ) )
    yydebug = 1;
  if ( !yyparse() )
    fprintf(stderr,"\t Program accepted !!!\n");
}