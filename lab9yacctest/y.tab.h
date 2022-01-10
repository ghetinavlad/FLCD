/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     IDENTIFIER = 258,
     CONSTANT = 259,
     START = 260,
     EXIT = 261,
     IF = 262,
     ELSE = 263,
     FOR = 264,
     WHILE = 265,
     READ = 266,
     WRITE = 267,
     INT = 268,
     STRING = 269,
     CONST = 270,
     ARRAY = 271,
     COLON = 272,
     SEMI_COLON = 273,
     COMA = 274,
     DOT = 275,
     LEFT_ROUND_PARENTHESIS = 276,
     RIGHT_ROUND_PARENTHESIS = 277,
     LEFT_SQUARE_PARENTHESIS = 278,
     RIGHT_SQUARE_PARENTHESIS = 279,
     LEFT_BRACKET = 280,
     RIGHT_BRACKET = 281,
     PLUS = 282,
     MINUS = 283,
     MULTIPLY = 284,
     DIVISION = 285,
     MODULO = 286,
     LESS_THAN = 287,
     GREATER_THAN = 288,
     LESS_OR_EQUAL_THAN = 289,
     GREATER_OR_EQUAL_THAN = 290,
     DIFFERENT = 291,
     ASSIGNMENT = 292,
     EQUAL = 293
   };
#endif
/* Tokens.  */
#define IDENTIFIER 258
#define CONSTANT 259
#define START 260
#define EXIT 261
#define IF 262
#define ELSE 263
#define FOR 264
#define WHILE 265
#define READ 266
#define WRITE 267
#define INT 268
#define STRING 269
#define CONST 270
#define ARRAY 271
#define COLON 272
#define SEMI_COLON 273
#define COMA 274
#define DOT 275
#define LEFT_ROUND_PARENTHESIS 276
#define RIGHT_ROUND_PARENTHESIS 277
#define LEFT_SQUARE_PARENTHESIS 278
#define RIGHT_SQUARE_PARENTHESIS 279
#define LEFT_BRACKET 280
#define RIGHT_BRACKET 281
#define PLUS 282
#define MINUS 283
#define MULTIPLY 284
#define DIVISION 285
#define MODULO 286
#define LESS_THAN 287
#define GREATER_THAN 288
#define LESS_OR_EQUAL_THAN 289
#define GREATER_OR_EQUAL_THAN 290
#define DIFFERENT 291
#define ASSIGNMENT 292
#define EQUAL 293




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

