# TPC 3

**Data:** 26/02/2025

## Aluno

**Nome:** Guilherme Oliveira

**ID:** a95021

**Fotografia:**

<img src=https://i.imgur.com/ag9VyrP.jpg alt="Fotografia" style="width:20%;">

### Resumo

O programa criado converte um ficheiro Markdown (_.md_) para um ficheiro HTML (_.html_) utilizando expressões regulares para detetar os elementos Markdown. A maior dificuldade está no processamento de listas numeradas, para isto usei um estado (**_in_list_**) que nos diz se nos encontramos a meio de uma lista.
O programa suporta a conversão dos seguintes elementos:

- **Cabeçalhos:** `#`, `##`, `###`, etc.
- **Negrito:** `**texto**` ou `__texto__`
- **Itálico:** `*texto*` ou `_texto_`
- **Links:** `[texto](url)`
- **Imagens:** `![texto alternativo](url)`
- **Listas numeradas:** `1. Item`, `2. Item`, `3. Item`

### Resultados (lista com apontadores para os ficheiros)
- [md_to_html.py](./md_to_html.py)
- [test.md](./test.md)
- [test.html](./test.html)