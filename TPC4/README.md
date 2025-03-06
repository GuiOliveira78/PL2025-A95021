# TPC 4

**Data:** 06/03/2025

## Aluno

**Nome:** Guilherme Oliveira

**ID:** a95021

**Fotografia:**

<img src=https://i.imgur.com/ag9VyrP.jpg alt="Fotografia" style="width:20%;">

### Resumo
Este TPC teve como objetivo construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:
```
# DBPedia: obras de Chuck Berry 
 
select ?nome ?desc where { 
    ?s a dbo:MusicalArtist. 
    ?s foaf:name "Chuck Berry"@en . 
    ?w dbo:artist ?s. 
    ?w foaf:name ?nome. 
    ?w dbo:abstract ?desc 
} LIMIT 1000 
```

Para a sua realização utilizei os exemplos de tokenizers fornecidos pelo docente.
Assim sendo comecei por escrever um ficheiro [tokens_query.json](./tokens_query.json) onde podemos encontrar os tokens escolhidos para o analizador léxico. De seguida alterei uns detalhes no ficheiro [gen_tokenizer.py](./gen_tokenizer.py), que tem como função criar o analisador léxico com os tokens escolhidos anteriormente, e executei-o, dando origem ao ficheiro [analex_query.py](./analex_query.py) onde temos o analisador léxico pedido.

### Resultados (lista com apontadores para os ficheiros)
- [tokens_query.json](./tokens_query.json)
- [gen_tokenizer.py](./gen_tokenizer.py)
- [analex_query.py](./analex_query.py)
- [test.txt](./test.txt)