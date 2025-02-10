import sys
import somador

def main():
    
    #ficheiro = input("Introduza o nome do ficheiro a converter -> ")
    ficheiro = 'exemplo.txt'
    #ficheiro = "../" + ficheiro
    
    sys.stdin = open(ficheiro, 'r')
    text = sys.stdin.read()
    sys.stdin = sys.__stdin__
    
    text_list = somador.split_text(text)
    
    print(text_list)
    
    somador.soma(text_list)

    return text
    
    
if __name__ == "__main__":
    main()