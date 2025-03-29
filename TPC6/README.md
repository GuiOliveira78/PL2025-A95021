# TPC 6

**Data:** 29/03/2025

## Aluno

**Nome:** Guilherme Oliveira

**ID:** a95021

**Fotografia:**

<img src=https://i.imgur.com/ag9VyrP.jpg alt="Fotografia" style="width:20%;">

### Resumo

Este projeto consiste na implementação de um analisador sintático para expressões aritméticas utilizando a biblioteca PLY. O programa reconhece expressões que envolvem operações de adição, subtração, multiplicação e divisão, suportando também parênteses para definir a precedência das operações. Em [sexp_lex.txt](./sexp_lex.txt) encontrámos a gramática que defini para abordar o problema.

O analisador léxico [sexp_lex.py](./sexp_lex.py) identifica os tokens correspondentes aos operadores matemáticos e números, enquanto o analisador sintático [sexp_sin.py](./sexp_sin.py) processa a estrutura da expressão de acordo com uma gramática definida.

Ao executar o programa, o utilizador pode inserir expressões matemáticas, e o parser irá avaliá-las, retornando o resultado correspondente e indicando se a expressão é válida.

### Resultados (lista com apontadores para os ficheiros)
- [sexp_lex.txt](./sexp_lex.txt)
- [sexp_lex.py](./sexp_lex.py)
- [sexp_sin.py](./sexp_sin.py)