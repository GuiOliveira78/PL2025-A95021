
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<LISTAR>[lL][iI][sS][tT][aA][rR])|(?P<MOEDA>[mM][oO][eE][dD][aA])|(?P<SELECIONAR>[sS][eE][lL][eE][cC][iI][oO][nN][aA][rR])|(?P<CODIGO>A\d+)|(?P<SAIR>[sS][aA][iI][rR])|(?P<EURO>\d+e)|(?P<CENT>\d+c)|(?P<VIRGULA>,)|(?P<PONTO>\.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['LISTAR']:
            t = ("LISTAR", dic['LISTAR'], linha, m.span())

        elif dic['MOEDA']:
            t = ("MOEDA", dic['MOEDA'], linha, m.span())
    
        elif dic['SELECIONAR']:
            t = ("SELECIONAR", dic['SELECIONAR'], linha, m.span())
    
        elif dic['CODIGO']:
            t = ("CODIGO", dic['CODIGO'], linha, m.span())
    
        elif dic['SAIR']:
            t = ("SAIR", dic['SAIR'], linha, m.span())
    
        elif dic['EURO']:
            t = ("EURO", dic['EURO'], linha, m.span())
    
        elif dic['CENT']:
            t = ("CENT", dic['CENT'], linha, m.span())
    
        elif dic['VIRGULA']:
            t = ("VIRGULA", dic['VIRGULA'], linha, m.span())
    
        elif dic['PONTO']:
            t = ("PONTO", dic['PONTO'], linha, m.span())
    
        reconhecidos.append(t)
    return reconhecidos
