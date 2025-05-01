"""
adicionar nomes dos amigos
copiar lista de amigos
botão sortear - mostra origem e destino entre os nomes
botão reiniciar
"""

from random import randint  

ordem_origem = []
ordem_destino = []

amigo_origem = []
amigo_destino = []

while True:
    amigo_temp = input('Digite o nome do amigo: ')
    amigo_origem.append(amigo_temp)
    amigo_destino = amigo_origem
    continuar = input('Deseja adicionar mais nomes? S/N: ')
    if continuar.upper() == 'N':
        break

print(amigo_origem)
print(amigo_destino)

while True:
    amigo_se_pegou = True
    while True:
        for i in range(len(amigo_origem)):
            num_temp = randint(0, len(amigo_origem)-1)
            if num_temp in ordem_origem:
                num_temp = randint(0, len(amigo_origem)-1)
            else:
                ordem_origem.append(num_temp)            
        if len(ordem_origem) == len(amigo_origem):
            break
    print(ordem_origem)    
    while True:
        for i in range(len(amigo_destino)):
            num_temp = randint(0, len(amigo_destino)-1)
            if num_temp in ordem_destino:
                num_temp = randint(0, len(amigo_destino)-1)
            else:
                ordem_destino.append(num_temp)            
        if len(ordem_destino) == len(amigo_destino):
            break
    print(ordem_destino)    
    for i in range(len(ordem_origem)):
        if ordem_origem[i] == ordem_destino[i]:
            amigo_se_pegou = True
            print('algum amigo se pegou, ')
            break
        
        else:
            amigo_se_pegou = False

    if amigo_se_pegou == False:
        print('Dessa vez deu certo')
        break
    else:
        ordem_origem = []
        ordem_destino = []
        print('refazendo...')

print(ordem_origem)
print(ordem_destino)               

for i in range(len(ordem_origem)):
    print(f'{amigo_origem[ordem_origem[i]]} pegou --> {amigo_destino[ordem_destino[i]]}')


