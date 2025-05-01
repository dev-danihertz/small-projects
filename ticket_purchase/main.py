
disponibilidade = {
"pista": [100],
"cadeira_superior": [200],
"cadeira_inferior": [400]
}

while True:
    cliente_compra_tipo = input("Digite o tipo de ingresso: ")
    cliente_compra_qtde = int(input("Digite a quantidade: "))

    if cliente_compra_tipo not in disponibilidade:
        print("produto inexistente")
    else:
        if cliente_compra_qtde > disponibilidade[cliente_compra_tipo][0]:
            print("Quantidade insuficiente" )

    novo_valor = disponibilidade[cliente_compra_tipo][0] - cliente_compra_qtde
    disponibilidade[cliente_compra_tipo][0] = novo_valor

    print(disponibilidade)
