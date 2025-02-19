# TPC 2

**Data:** 19/02/2025

****

## Aluno

**Nome:** Guilherme Oliveira

**ID:** a95021

**Fotografia:**

<img src=https://i.imgur.com/ag9VyrP.jpg alt="Fotografia" style="width:20%;">

****

### Resumo
Neste TPC construí um programa que trata os dados de um _CSV_ e, através de um menu, permite obtê-los no terminal.
Primeiramente elaborei uma expressão regular para captar cada registo do _CSV_ tendo chegado à seguinte expressão, onde cada grupo de captura representa um campo.
- `^([^;]+);"?([\s\S]*?)"?;([^;]+);([^;]+);([^;]+);([^;]+);([^;]+)$`

Em seguida criei o ficheiro **[csv_aux.py](./csv_aux.py)** onde temos as seguintes funções e respetivas funcionalidades:
- **[parse_text](./csv_aux.py#L11#L26)** - recebe um texto com o conteúdo do csv e, utilizando a expressão regular definida anteriormente, faz o _parsing_ do mesmo criando uma lista em que cada registo é definido por um dicionário;
- **[lista_compositores](./csv_aux.py#L31#L37)** - recebe a lista criada acima e devolve uma lista apenas com os autores existentes;
- **[print_compositores](./csv_aux.py#L39#L44)** - tem como função apenas fazer _print_ de forma organizada dos dados produzidos acima;
- **[numero_obras_periodo](./csv_aux.py#L49#L56)** - recebe a lista de registos e devolve um dicionário onde as chaves são os períodos existentes e os valores o número de obras desse período;
- **[print_nobras_periodo](./csv_aux.py#L58#L61)** - tem como função apenas fazer _print_ de forma organizada dos dados produzidos acima;
- **[obras_por_periodo](./csv_aux.py#L66#L72)** - recebe a lista de registos e devolve um dicionário onde as chaves são os períodos existentes e os valores são listas com os títulos das obras desse período;
- **[print_obras_periodo](./csv_aux.py#L74#L80)** - tem como função apenas fazer _print_ de forma organizada dos dados produzidos acima.
- **[print_obras](./csv_aux.py#85#88)** - tem como função apenas fazer _print_ de forma organizada de todas as obras.

Por fim criei o ficheiro **[main.py](./main.py)** onde primeiramente é feita a leitura do ficheiro [obras.csv](./obras.csv). Em seguida executámos a função [parse_text](./csv_aux.py#L11#L26) para fazermos efetivamente o _parsing_ dos dados, que são guardados na variável [items](./main.py#L12).
Por fim podemos encontrar o [menu](./main.py#L16#L39) onde são listadas e respondidas as opções pedidas no enunciado.

### Resultados (lista com apontadores para os ficheiros)
- [csv_aux.py](./csv_aux.py)
- [main.py](./main.py)
- [obras.csv](./obras.csv)