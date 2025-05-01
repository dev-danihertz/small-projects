from random import randint

while True:
    num_sorteados = []

    qtde_numeros = int(input("Digite a quantidade de números a serem sorteados: "))
    num_inicial = int(input("Digite um número inicial: "))
    num_final = int(input("Digite um número final: "))

    # qtde_numeros = 10
    # num_inicial = 1
    # num_final = 10
    num_final_temp = 0

    for i in range(qtde_numeros):
        while True:
            num_final_temp = (randint(num_inicial, num_final))
            if num_final_temp not in num_sorteados:
                break
        num_sorteados.append(num_final_temp)
        print(num_final_temp)

    print(num_sorteados)
    continuar = input("Deseja continuar? [S/N]: ")
    if continuar.upper() == "N":
        break