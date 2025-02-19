import sys
import csv_aux

def main():
    
    ficheiro = 'obras.csv'
    
    sys.stdin = open(ficheiro, 'r')
    text = sys.stdin.read()
    sys.stdin = sys.__stdin__
    
    items = csv_aux.parse_text(text)
    print(items[1])

    def mostrar_menu():
        while True:
            print("\nMenu:")
            print("1. Lista ordenada alfabeticamente dos compositores musicais")
            print("2. Distribuição das obras por período")
            print("3. Dicionário de obras por período")
            print("4. Listar Obras")
            print("5. Sair")
            print()
            opcao = input("Escolha uma opção: ")
            print()
            if opcao == "1":
                res = csv_aux.lista_compositores(items)
                csv_aux.print_compositores(res)
            elif opcao == "2":
                res = csv_aux.numero_obras_periodo(items)
                csv_aux.print_nobras_periodo(res)
            elif opcao == "3":
                res = csv_aux.obras_por_periodo(items)
                csv_aux.print_obras_periodo(res)
            elif opcao == "4":
                csv_aux.print_obras(items)
            elif opcao == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

    mostrar_menu()
    

    


    
    
if __name__ == "__main__":
    main()