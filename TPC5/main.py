import sys
from datetime import datetime
from analex_stock import tokenize
import vending

def main():
    stock = vending.load_stock()
    saldo = 0
    
    date = datetime.now().strftime("%d-%m-%Y")
    print()
    print(f"maq: {date}, Stock carregado, Estado atualizado. ")
    print("maq: Bom dia. Estou disponível para atender o seu pedido. ")

    inserir_moeda = False
    selecting = False
    while (True):
        print("\n>> ", end="")
        line = input()
        for tok in tokenize(line):
            if tok[0] == "LISTAR":
                vending.listar_stock(stock)
            elif tok[0] == "SAIR":
                vending.save_stock(stock)
                print(vending.calcula_troco(saldo))
                print("maq: Até à próxima.")
                exit()
            elif tok[0] == "SELECIONAR": ###### TO DO ######
                selecting = True
            elif tok[0] == "CODIGO" and selecting: ###### TO DO ######
                saldo = vending.selecionar_produto(stock, tok[1], saldo)
                selecting = False
            elif tok[0] == "MOEDA":
                inserir_moeda = True
            elif (tok[0] == "EURO" or tok[0] == "CENT") and inserir_moeda:
                saldo = vending.add_moeda(saldo, tok[1])
            elif tok[0] == "PONTO" and inserir_moeda:
                inserir_moeda = False
                vending.print_saldo(saldo)
            elif tok[0] == "VIRGULA":
                pass
            else:
                print("maq: Comando inválido.")
    
    
if __name__ == "__main__":
    main()
    sys.exit(0)