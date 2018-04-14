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

#-------------------------------------------------------------
# Token Object Class -- Reads source program and build tokens 
#-------------------------------------------------------------

class Scanner(object):
    def __init__(self,value_of,type_of,row,column):
        self.row      = row
        self.column   = column
        self.type_of  = type_of
        self.value_of = value_of
    
    def __unicode__(self):
        return '<%s,%s,%i,%i>' % (self.value_of,self.type_of,self.row,self.column)
    
    def __repr__(self):
        return self.__unicode__()

def token_name(suffix):
    # Returns token prefix + given suffix
    return TOKEN_NAME_PREFIX + suffix.upper()

# Store reserved words with some system variables
reserved_tokens = {
    'char'   : TOKEN_DATA_TYPE_CHAR,
    'real'   : TOKEN_DATA_TYPE_REAL,
    'integer': TOKEN_DATA_TYPE_INT,
    'boolean': TOKEN_DATA_TYPE_BOOL
                  }
for keyword, value in symbol_map.items():
    if value == RESERVED:
        reserved_tokens[keyword.lower()] = TOKEN_RESERVED
        reserved_tokens[keyword.upper()] = TOKEN_RESERVED

# Operators dictionary
operators_classifications = {
    '<=': TOKEN_OPERATOR_LTE,
    '>=': TOKEN_OPERATOR_GTE,
    '+' : TOKEN_OPERATOR_PLUS,
    ',' : TOKEN_OPERATOR_COMMA,
    ':' : TOKEN_OPERATOR_COLON,
    '-' : TOKEN_OPERATOR_MINUS,
    '/' : TOKEN_OPERATOR_DIVISION,
    '=' : TOKEN_OPERATOR_EQUALITY,
    '<>': TOKEN_OPERATOR_NOT_EQUAL,
    ':=': TOKEN_OPERATOR_ASSIGNMENT,
    '(' : TOKEN_OPERATOR_LEFT_PAREN,
    ')' : TOKEN_OPERATOR_RIGHT_PAREN,
    '[' : TOKEN_OPERATOR_LEFT_BRACKET,
    '<' : TOKEN_OPERATOR_LEFT_CHEVRON,
    '>' : TOKEN_OPERATOR_RIGHT_CHEVRON,
    ']' : TOKEN_OPERATOR_RIGHT_BRACKET,
    '*' : TOKEN_OPERATOR_MULTIPLICATION
                                }