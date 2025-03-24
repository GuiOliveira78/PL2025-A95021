# TPC 5

**Data:** 24/03/2025

## Aluno

**Nome:** Guilherme Oliveira

**ID:** a95021

**Fotografia:**

<img src=https://i.imgur.com/ag9VyrP.jpg alt="Fotografia" style="width:20%;">

### Resumo
Este trabalho teve como objetivo criar um sistema para uma máquina de vending.
Para isto comecei por definir os tokens da minha linguagem em [tokens_stock.json](./tokens_stock.json), que utilizei de seguida para criar o meu analizador léxico ([analex_stock.py](./analex_stock.py)) através do [gen_tokenizer.py](./gen_tokenizer.py).
Após ter o meu analisador foi só tratar da parte mais funcional. Em [main.py](./main.py) encontrámos o cérebro da máquina onde é decidido o que fazer com cada _Token_, e em [vending.py](./vending.py) encontrámos algumas funções de _backend_ da máquina. Em [stock.json](./stock.json) podemos ainda encontrar o stock da máquina que é carregado a cada inicialização e gravada quando é terminada a utilização da mesma.

### Resultados (lista com apontadores para os ficheiros)
- [tokens_stock.json](./tokens_stock.json)
- [gen_tokenizer.py](./gen_tokenizer.py)
- [analex_stock.py](./analex_stock.py)
- [main.py](./main.py)
- [vending.py](./vending.py)
- [stock.json](./stock.json)