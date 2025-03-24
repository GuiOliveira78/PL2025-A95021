import json

moedas = {
    "2e": 200,
    "1e": 100,
    "50c": 50,
    "20c": 20,
    "10c": 10,
    "5c": 5,
    "2c": 2,
    "1c": 1
}


# Função que carrega o stock do ficheiro stock.json
def load_stock():
    with open("stock.json", "r") as file:
        stock = json.load(file)
    return stock

# Função que guarda o stock no ficheiro stock.json
def save_stock(stock):
    with open("stock.json", "w", encoding="utf-8") as file:
        json.dump(stock, file, indent=4, ensure_ascii=False) 
        
# Função que lista o stock
def listar_stock(stock):
    print("maq: ")
    print("-" * 50)
    print(f"{'cod':<8}| {'nome':<20}| {'quant':<10}| {'preco':<6}")
    print("-" * 50)
    for produto in stock:
        print(f"{produto['codigo']:<8}| {produto['nome']:<20}| {produto['quant']:<10}| {produto['preco']/100:<6}")
    print("-" * 50)
        
        
# Função que calcula o troco
def calcula_troco(saldo):
    troco = saldo
    output = []
    moedas = [200, 100, 50, 20, 10, 5, 2, 1]
    troco_moedas = []
    for moeda in moedas:
        troco_moedas.append(troco // moeda)
        troco = troco % moeda
        
    for i, moeda in zip(troco_moedas, moedas):
        if i != 0 and moeda >= 100:
            output.append(f"{i}x {moeda//100}e")
        elif i != 0:
            output.append(f"{i}x {moeda}c")
    
    if not output:
        out = "maq: Não há troco."
    elif len(output) == 1:
        out = f"maq: Pode retirar o troco: {output[0]}."
    else:
        out = f"maq: Pode retirar o troco: {', '.join(output[:-1])} e {output[-1]}."
    
    return out

# Função que adiciona moedas ao saldo
def add_moeda(saldo, moeda):
    saldo += moedas[moeda]
    return saldo

# Função que imprime o saldo
def print_saldo(saldo):
    if saldo > 100:
        print(f"maq: Saldo = {saldo//100}e{saldo%100}c")
    else:
        print(f"maq: Saldo = {saldo}c")

# Função que imprime o pedido
def print_pedido(preco):
    if preco > 100:
        print(f"maq: Pedido = {preco//100}e{preco%100}c")
    else:
        print(f"maq: Pedido = {preco}c")

# Função que verifica se o saldo é suficiente
def check_saldo(saldo, preco):
    if saldo >= preco:
        return True
    return False

# Função que seleciona um produto
def selecionar_produto(stock, codigo, saldo):
    # verificar se o produto existe no stock
    produto = None
    for product in stock:
        if product["codigo"] == codigo:
            produto = product
            break
    # produto não existe
    if produto is None:    
        print("maq: Produto não existe.")
        return saldo
    # verificar se há stock
    if produto["quant"] == 0:
        print("maq: Produto esgotado.")
        return saldo
    # verificar se o saldo é suficiente
    if check_saldo(saldo, produto["preco"]):
        produto["quant"] -= 1
        saldo -= produto["preco"]
        print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
        print_saldo(saldo)
        return saldo
    # saldo insuficiente
    else:
        print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
        print_saldo(saldo)
        print_pedido(produto["preco"])
        return saldo