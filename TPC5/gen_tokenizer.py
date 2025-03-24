import json


tokens = []
with open("tokens_stock.json") as f:
    tokens = json.load(f)
    
if not tokens:
    raise ValueError("Arquivo tokens_stock.json está vazio ou mal formatado")

tokens_regex = '|'.join([f'(?P<{t['id']}>{t['expreg']})' for t in tokens])

code = f"""
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'{tokens_regex}', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['{tokens[0]['id']}']:
            t = ("{tokens[0]['id']}", dic['{tokens[0]['id']}'], linha, m.span())
"""

for t in tokens[1:]:
    code += f"""
        elif dic['{t['id']}']:
            t = ("{t['id']}", dic['{t['id']}'], linha, m.span())
    """
code += f"""
        reconhecidos.append(t)
    return reconhecidos

with open('test.txt', 'r', encoding='utf-8') as file:
    for linha in file:
        for tok in tokenize(linha):
            print(tok)    
"""
print(code)

with open("analex_query.py", "w") as f:
    f.write(code)