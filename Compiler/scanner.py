# coding=utf-8  ** DO NOT REMOVE **

#--------------------------------------
#               Scanner                
#--------------------------------------

import os

#----------------------------------------------
# Initial setup for symbol & reserved keywords
#----------------------------------------------

LETTER = 0
RESERVED = 1
SPACE = 2
DIGIT = 3
OPERATOR = 4
QUOTE = 5
EOL = 6
DOT = 7
COMMENT = 8
COMMENT_TYPES = ['//', '{*', '(*']
SEMICOLON = 9
NEGATIVE = 10
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
OPERATORS = '+-/,()<>:=*[]'

symbol_map = {' ': SPACE,
              '\t': SPACE,
              '\r': SPACE,
              '\n': EOL,
              '\'': QUOTE,
              '.': DOT,
              '{': COMMENT,
              ';': SEMICOLON,
              '-': NEGATIVE
             }

for character in ALPHABET:
    symbol_map[character] = LETTER
    symbol_map[character.lower()] = LETTER

for operator in OPERATORS:
    symbol_map[operator] = OPERATOR

for digit in range(0, 10):
    symbol_map[digit] = DIGIT
    symbol_map[str(digit)] = DIGIT

with open(os.path.dirname(__file__) + '/keywords.txt') as keyword_file:
    for line in keyword_file.readlines():
        # Read every line while stripping whitespace and store reserved keywords
        symbol_map[line.strip()] = RESERVED

#---------------------------------------------
# Token Operators, Data-Types, Reserved Words
#---------------------------------------------

TOKEN_NAME_PREFIX = 'TK_'
TOKEN_ID = TOKEN_NAME_PREFIX + 'ID'
TOKEN_DOT = TOKEN_NAME_PREFIX + 'DOT'
TOKEN_EOF = TOKEN_NAME_PREFIX + 'EOF'
TOKEN_OPERATOR_GTE = TOKEN_NAME_PREFIX + '>='
TOKEN_OPERATOR_LTE = TOKEN_NAME_PREFIX + '<='
TOKEN_COMMENT = TOKEN_NAME_PREFIX + 'COMMENT'
TOKEN_OPERATOR_PLUS = TOKEN_NAME_PREFIX + '+'
TOKEN_OPERATOR_MINUS = TOKEN_NAME_PREFIX + '-'
TOKEN_REAL_LIT = TOKEN_NAME_PREFIX + 'REAL_LIT'
TOKEN_OPERATOR = TOKEN_NAME_PREFIX + 'OPERATOR'
TOKEN_STRING_LIT = TOKEN_NAME_PREFIX + 'STR_LIT'
TOKEN_SEMICOLON = TOKEN_NAME_PREFIX + 'SEMICOLON'
TOKEN_OPERATOR_DIVISION = TOKEN_NAME_PREFIX + '/'
TOKEN_OPERATOR_EQUALITY = TOKEN_NAME_PREFIX + '='
TOKEN_CHARACTER = TOKEN_NAME_PREFIX + 'CHARACTER'
TOKEN_OPERATOR_COLON = TOKEN_NAME_PREFIX + 'COLON'
TOKEN_OPERATOR_COMMA = TOKEN_NAME_PREFIX + 'COMMA'
TOKEN_OPERATOR_NOT_EQUAL = TOKEN_NAME_PREFIX + '<>'
TOKEN_OPERATOR_LEFT_BRACKET = TOKEN_NAME_PREFIX + '['
TOKEN_OPERATOR_LEFT_CHEVRON = TOKEN_NAME_PREFIX + '<'
TOKEN_OPERATOR_RIGHT_CHEVRON = TOKEN_NAME_PREFIX + '>'
TOKEN_OPERATOR_RIGHT_BRACKET = TOKEN_NAME_PREFIX + ']'
TOKEN_OPERATOR_MULTIPLICATION = TOKEN_NAME_PREFIX + '*'
TOKEN_OPERATOR_LEFT_PAREN = TOKEN_NAME_PREFIX + 'LPAREN'
TOKEN_OPERATOR_RIGHT_PAREN = TOKEN_NAME_PREFIX + 'RPAREN'
TOKEN_OPERATOR_ASSIGNMENT = TOKEN_NAME_PREFIX + 'ASSIGNMENT'


TOKEN_DATA_TYPE_INT = TOKEN_NAME_PREFIX + 'INTEGER'
TOKEN_DATA_TYPE_RANGE = TOKEN_NAME_PREFIX + 'RANGE'
TOKEN_DATA_TYPE_ARRAY = TOKEN_NAME_PREFIX + 'ARRAY'
TOKEN_DATA_TYPE_REAL = TOKEN_NAME_PREFIX + 'REAL'
TOKEN_DATA_TYPE_CHAR = TOKEN_NAME_PREFIX + 'CHAR'
TOKEN_DATA_TYPE_BOOL = TOKEN_NAME_PREFIX + 'BOOLEAN'

TOKEN_RESERVED = TOKEN_NAME_PREFIX + 'RESERVED'

string_store = set()

class Token(object):
    pass