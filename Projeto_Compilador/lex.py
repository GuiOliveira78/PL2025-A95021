import ply.lex as lex

tokens = [
    'PROGRAM', 'VAR', 'BEGIN', 'END', 
    # ciclos e condicionais
    'IF', 'THEN', 'ELSE', 'WHILE', 'DO', 'FOR', 'TO', 
    # funções
    'FUNCTION', 'DIV', 'MOD', 'LENGTH',
    # tipos
    'INTEGER', 'STRING', 'BOOLEAN',
    # bools
    'TRUE', 'FALSE',
    # in&out
    'WRITELN', 'WRITE', 'READLN', 'READ',
    # aritmeticos e relacionais
    'PLUS', 'MINUS', 'TIMES', 'ASSIGN',
    'GT', 'LT', 'EQ', 'NEQ', 'GTE', 'LTE',
    # literals
    'SEMICOLON', 'DOT', 'COLON', 'COMMA', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'DOTDOT', 'STRING_LITERAL',
    # lógicos
    'AND', 'OR',
    'ARRAY', 'OF',
    'ID', 'NUMBER'
]

t_ignore = ' \r\n\t'
# PR
keywords = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'for': 'FOR',
    'to': 'TO',
    'function': 'FUNCTION',
    'div': 'DIV',
    'mod': 'MOD',
    'integer': 'INTEGER',
    'string': 'STRING',
    'boolean': 'BOOLEAN',
    'true': 'TRUE',
    'false': 'FALSE',
    'writeln': 'WRITELN',
    'write': 'WRITE',
    'readln': 'READLN',
    'read': 'READ',
    'array': 'ARRAY',
    'of': 'OF',
    'and': 'AND',
    'length': 'LENGTH'

}
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_ASSIGN = r':='
t_EQ = r'='
t_NEQ = r'<>'
t_GT = r'>'
t_LT = r'<'
t_GTE = r'>='
t_LTE = r'<='
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_DOT = r'\.'
t_COLON = r':'
t_DOTDOT = r'\.\.'
t_OR = r'or'
t_AND = r'and'

def t_STRING_LITERAL(t):
    r"'[^']*'"
    t.value = t.value[1:-1]
    return t

def t_MOD(t):
    r'mod'
    t.type="MOD"
    return t

def t_DIV(t):
    r'div'
    t.type="DIV"
    return t

def t_COMMENT(t):
    r'(\{.*?\})|(\(\*.*?\*\))'
    pass 

def t_NUMBER(t):
    r'\d+\.\d+|\d+' 
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_ARRAY(t):
    r'array'
    t.type="ARRAY"
    return t

def t_OF(t):
    r'of'
    t.type="OF"
    return t

def t_PROGRAM(t):
    r'program'
    t.type = 'PROGRAM'
    return t

def t_VAR(t):
    r'var'
    t.type = 'VAR'
    return t

def t_BEGIN(t):
    r'begin'
    t.type = 'BEGIN'
    return t

def t_END(t):
    r'end'
    t.type = 'END'
    return t

def t_IF(t):
    r'if'
    t.type = 'IF'
    return t

def t_THEN(t):
    r'then'
    t.type = 'THEN'
    return t

def t_ELSE(t):
    r'else'
    t.type = 'ELSE'
    return t

def t_WHILE(t):
    r'while'
    t.type = 'WHILE'
    return t

def t_DO(t):
    r'do'
    t.type = 'DO'
    return t

def t_FOR(t):
    r'for'
    t.type = 'FOR'
    return t

def t_TO(t):
    r'to'
    t.type = 'TO'
    return t

def t_FUNCTION(t):
    r'function'
    t.type = 'FUNCTION'
    return t

def t_INTEGER(t):
    r'integer'
    t.type = 'INTEGER'
    return t

def t_STRING(t):
    r'string'
    t.type = 'STRING'
    return t

def t_BOOLEAN(t):
    r'boolean'
    t.type = 'BOOLEAN'
    return t

def t_TRUE(t):
    r'true'
    t.type = 'TRUE'
    return t

def t_FALSE(t):
    r'false'
    t.type = 'FALSE'
    return t

def t_WRITELN(t):
    r'writeln'
    t.type = 'WRITELN'
    return t

def t_WRITE(t):
    r'write'
    t.type = 'WRITE'
    return t

def t_READLN(t):
    r'readln'
    t.type = 'READLN'
    return t

def t_READ(t):
    r'read'
    t.type = 'READ'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = t.value.lower()
    t.type = keywords.get(t.value, 'ID')
    return t

def t_error(t):
    print(f'Illegal character: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()
