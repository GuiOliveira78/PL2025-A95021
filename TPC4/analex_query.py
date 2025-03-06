
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<COMMENT>\#.*)|(?P<SELECT>[sS][eE][lL][eE][cC][tT])|(?P<LIMIT>[lL][iI][mM][iI][tT])|(?P<WHERE>[wW][hH][eE][rR][eE])|(?P<RBRACKET>\{)|(?P<LBRACKET>\})|(?P<NUMBER>\d+)|(?P<VARIABLE>\?[a-z]+)|(?P<URI>[a-zA-Z0-9]+:[a-zA-Z0-9]+)|(?P<LANG>"[^"]*"@[a-zA-Z]+)|(?P<A>a)|(?P<DOT>\.)|(?P<NEWLINE>\n+)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['COMMENT']:
            t = ("COMMENT", dic['COMMENT'], linha, m.span())

        elif dic['SELECT']:
            t = ("SELECT", dic['SELECT'], linha, m.span())
    
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())
    
        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], linha, m.span())
    
        elif dic['RBRACKET']:
            t = ("RBRACKET", dic['RBRACKET'], linha, m.span())
    
        elif dic['LBRACKET']:
            t = ("LBRACKET", dic['LBRACKET'], linha, m.span())
    
        elif dic['NUMBER']:
            t = ("NUMBER", dic['NUMBER'], linha, m.span())
    
        elif dic['VARIABLE']:
            t = ("VARIABLE", dic['VARIABLE'], linha, m.span())
    
        elif dic['URI']:
            t = ("URI", dic['URI'], linha, m.span())
    
        elif dic['LANG']:
            t = ("LANG", dic['LANG'], linha, m.span())
    
        elif dic['A']:
            t = ("A", dic['A'], linha, m.span())
    
        elif dic['DOT']:
            t = ("DOT", dic['DOT'], linha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    
        reconhecidos.append(t)
    return reconhecidos

with open('test.txt', 'r', encoding='utf-8') as file:
    for linha in file:
        for tok in tokenize(linha):
            print(tok)    
