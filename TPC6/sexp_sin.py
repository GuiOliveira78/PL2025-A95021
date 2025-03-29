import ply.yacc as yacc
from sexp_lex import tokens
from functools import reduce

# Production rules
def p_global(p):
    "S : Exp"
    print('Resultado:', p[1])
    
def p_Exp_ADD(p):
    '''
    Exp : Exp ADD Termo
    '''
    p[0] = p[1] + p[3]
    
def p_Exp_SUB(p):
    '''
    Exp : Exp SUB Termo
    '''
    p[0] = p[1] - p[3]
    
def p_Exp_Termo(p):
    '''
    Exp : Termo
    '''
    p[0] = p[1]

def p_Termo_MUL(p):
    '''
    Termo : Termo MUL Fator
    '''
    p[0] = p[1] * p[3]

def p_Termo_DIV(p):
    '''
    Termo : Termo DIV Fator
    '''
    p[0] = p[1] / p[3]
        
def p_Termo_Fator(p):
    '''
    Termo : Fator
    '''
    p[0] = p[1]
    
def p_Fator_NUM(p):
    '''
    Fator : NUM
    '''
    p[0] = p[1]
    
def p_Fator_LPAREN(p):
    '''
    Fator : LPAREN Exp RPAREN
    '''
    p[0] = p[2]
        
def p_error(p):
    print('Erro sintático:', p)
    parser.success = False
    
# Build the parser
parser = yacc.yacc(debug=True)

# Read line from input and parse it
import sys
for linha in sys.stdin:
    parser.success = True
    parser.parse(linha)
    if parser.success:
        print('Frase válida: ', linha)
    else:
        print('Frase inválida... Corrija e tente novamente!')