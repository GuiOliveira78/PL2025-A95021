import re
import sys

'''
^([^;]+);"?([\s\S]*?)"?;([^;]+);([^;]+);([^;]+);([^;]+);([^;]+)$
Expressão regular para capturar uma obra do ficheiro CSV onde cada grupo de captura corresponde a um campo da obra.
'''
#---------------------------------------------
# Função para fazer o parse do texto do ficheiro CSV
#---------------------------------------------
def parse_text(text):
    items = re.findall(r'^([^;]+);"?([\s\S]*?)"?;([^;]+);([^;]+);([^;]+);([^;]+);([^;]+)$', text, re.MULTILINE)
    items.remove(items[0])

    for i, item in enumerate(items):
        items[i] = {
            'nome': item[0],
            'desc': item[1],
            'anoCriacao': item[2],
            'periodo': item[3],
            'compositor': item[4],
            'duracao': item[5],
            '_id': item[6]
        }

    return items

#---------------------------------------------
# Função para listar os compositores e respetivo print
#---------------------------------------------
def lista_compositores(items):
    compositores = []
    for row in items:
        if row['compositor'] not in compositores:
            compositores.append(row['compositor'])
    compositores.sort()
    return compositores

def print_compositores(l):
    print("Compositores:")
    for compositor in l:
        print(f"    · {compositor}")
    print()
    print(f"Total de compositores: {len(l)}")

#---------------------------------------------
# Função para contar o número de obras por período e respetivo print
#---------------------------------------------
def numero_obras_periodo(items):
    periodos = {}
    for row in items:
        if row['periodo'] not in periodos:
            periodos[row['periodo']] = 1
        else:
            periodos[row['periodo']] += 1
    return periodos

def print_nobras_periodo(d):
    print("Número de obras por período:")
    for key, value in d.items():
        print(f"    · {key}: {value}")
        
#---------------------------------------------
# Função para listar as obras por período e respetivo print
#---------------------------------------------
def obras_por_periodo(items):
    periodos = {}
    for row in items:
        if row['periodo'] not in periodos:
            periodos[row['periodo']] = []
        periodos[row['periodo']].append(row['nome'])
    return periodos

def print_obras_periodo(d):
    print("Obras por período:")
    for key, value in d.items():
        print(f"    · {key}:")
        for obra in value:
            print(f"        · {obra}")
        print()
        
#---------------------------------------------
# Print para listar todas as obras 
#---------------------------------------------
def print_obras(items):
    print("Obras:")
    for i, row in enumerate(items):
        print(f"    {i+1} - {row['nome']} ({row['anoCriacao']}) - {row['compositor']}")