    
casas = [0,1,2,3,4,5,6,7,8]
vencedor = False


def print_jogo():
    print("", casas[0], casas[1], casas[2],"\n",casas[3], casas[4], casas[5], "\n", casas[6], casas[7], casas[8])

def p1_escolheu():
    if escolha == 0:
        casas[escolha] = "X"
    elif escolha == 1:
        casas[escolha] = "X"
    elif escolha == 2:
        casas[escolha] = "X"
    elif escolha == 3:
        casas[escolha] = "X"
    elif escolha == 4:
        casas[escolha] = "X"
    elif escolha == 5:
        casas[escolha] = "X"
    elif escolha == 6:
        casas[escolha] = "X"
    elif escolha == 7:
        casas[escolha] = "X"
    elif escolha == 8:
        casas[escolha] = "X"

def p2_escolheu():
    if escolha == 0:
        casas[escolha] = "O"
    elif escolha == 1:
        casas[escolha] = "O"
    elif escolha == 2:
        casas[escolha] = "O"
    elif escolha == 3:
        casas[escolha] = "O"
    elif escolha == 4:
        casas[escolha] = "O"
    elif escolha == 5:
        casas[escolha] = "O"
    elif escolha == 6:
        casas[escolha] = "O"
    elif escolha == 7:
        casas[escolha] = "O"
    elif escolha == 8:
        casas[escolha] = "O"

def verifica_p1_vencedor():
    global vencedor
    if ((casas[0] == "X" and casas[1] == "X" and casas[2] == "X") or
        (casas[3] == "X" and casas[4] == "X" and casas[5] == "X") or
        (casas[6] == "X" and casas[7] == "X" and casas[8] == "X") or
        (casas[0] == "X" and casas[3] == "X" and casas[6] == "X") or  
        (casas[1] == "X" and casas[4] == "X" and casas[7] == "X") or  
        (casas[2] == "X" and casas[5] == "X" and casas[8] == "X") or  
        (casas[0] == "X" and casas[4] == "X" and casas[8] == "X") or  
        (casas[2] == "X" and casas[4] == "X" and casas[6] == "X")):    
        print("Parabéns p1, você venceu")
        vencedor = True

def verifica_p2_vencedor():
    global vencedor
    if ((casas[0] == "O" and casas[1] == "O" and casas[2] == "O") or
        (casas[3] == "O" and casas[4] == "O" and casas[5] == "O") or
        (casas[6] == "O" and casas[7] == "O" and casas[8] == "O") or
        (casas[0] == "O" and casas[3] == "O" and casas[6] == "O") or  
        (casas[1] == "O" and casas[4] == "O" and casas[7] == "O") or  
        (casas[2] == "O" and casas[5] == "O" and casas[8] == "O") or  
        (casas[0] == "O" and casas[4] == "O" and casas[8] == "O") or  
        (casas[2] == "O" and casas[4] == "O" and casas[6] == "O")):    
        print("Parabéns p2, você venceu")
        vencedor = True

print_jogo()

while True:
    escolha = int(input("P1, Digite qual casa você escolhe jogar: "))

    # Verifica se a casa está vazia
    if casas[escolha] == "X" or casas[escolha] == "O":
        print("Essa casa não é válida!")
        continue

    p1_escolheu()
    print_jogo() 

    # VERIFICA SE P1 VENCEU
    verifica_p1_vencedor()
    if vencedor == True:
        break

    escolha = int(input("P2, Digite qual casa você escolhe jogar: "))

    # Verifica se a casa está vazia
    if casas[escolha] == "X" or casas[escolha] == "O":
        print("Essa casa não é válida!")
        continue

    p2_escolheu()
    print_jogo()

    # VERIFICA SE P2 VENCEU
    verifica_p2_vencedor()
    if vencedor == True:
        break

