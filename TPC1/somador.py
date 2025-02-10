import re

# Função que transforma um texto numa lista onde aparecem apenas os 'on', 'off', '=' e números
def split_text(text):
    lista = re.findall(r'\b[oO][nN](?=\s)|\b[oO][fF][fF](?=\s)|\d+,?\.?\d*|(?<=\s)=(?=\s)', text, flags=re.MULTILINE)
    return lista

# Função que recebe uma lista com 'on', 'off', '=' e números e 
# devolve a soma dos numeros que se encontrarem no estado on
def soma(text_list):
    estado_soma = False
    soma = 0
    for elem in text_list:
        if re.match(r'[oO][nN]', elem):                     # Se elem for 'on' ligamos o estado de somar
            estado_soma = True
        elif re.match(r'[oO][fF][fF]', elem):               # # Se elem for 'off' desligamos o estado de somar
            estado_soma = False
        elif (re.match(r'\d+,?\d*', elem) and estado_soma): # Se elem for um número e o estado estiver 'on' somamo-lo à soma total
            numero = float(elem.replace(',', '.'))
            soma += numero
        elif re.match(r'=', elem):                          # Se elem for '=' devolvemos o resultado atual da soma
            print('Soma: ' + str(soma))
    return soma

