
def adicionar_produto_ao_carrinho(carrinho, produto, quantidade):
    carrinho[produto] = quantidade

def limpar_carrinho(carrinho):
    carrinho.clear()

def calcular_total_do_carrinho(carrinho, produtos):
    total = 0
    for produto, quantidade in carrinho.items():
        preco = produtos[produto]
        total += preco * quantidade
    return total

carrinho = {}

produtos = {
    'fone': 1000,
    'celular': 1000,
    'oculos': 1000,
    'microfone': 1000
}
print()
for chave, valor in produtos.items():
    print({chave: valor})
    
print()
while True:
    while True:
        prod = input('Produto: ')
        qtde = int(input('Quantidade: '))
        adicionar_produto_ao_carrinho(carrinho, prod, qtde)
        print(carrinho)
        total = calcular_total_do_carrinho(carrinho, produtos)
        print(total)
        add_mais = input('Deseja adicionar mais um produto? [S/N]: ').upper()
        if add_mais.upper() == 'N':
            break
       
    acao_limpa_carrinho = input('Deseja limpar o carrinho? [S/N]: ').upper()

    if acao_limpa_carrinho == 'S':
        limpar_carrinho(carrinho)
        print(carrinho)
    else:
        break

"""
possibilidades de melhorias:
tratar erros caso escreva número errado do item
colocar cada item em um indice
colocar valores dentro do carrinho
adicionar mais produtos do mesmo item ao carrinho (ele substitui e não adiciona)
"""