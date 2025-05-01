
todos_os_jogos = []

class Jogos:
    def __init__(self, nome, status):
        self.nome = nome
        self.status = status

    def atualizar_status(self):
        if self.status == 'Aberto':
            self.status = 'Fechado'
        elif self.status == 'Fechado':
            self.status = 'Aberto'
        else:
            print('Status inválido!')

    def obter_status(self):
        return self.status

def listar_jogos():
    for indice, jogo in enumerate(todos_os_jogos):
        print(f'Jogo {indice + 1}: {jogo.nome} está {jogo.status}')

jogo1 = Jogos('Naruto', 'Aberto')
todos_os_jogos.append(jogo1)
jogo2 = Jogos('Star Wars', 'Aberto')
todos_os_jogos.append(jogo2)
jogo3 = Jogos('Pokemon', 'Fechado')
todos_os_jogos.append(jogo3)

while True:
    listar_jogos()

    num_jogo_alterar = int(input('Digite o número do jogo que deseja alterar: '))
    if 1 <= num_jogo_alterar <= len(todos_os_jogos):
        jogo_selecionado = todos_os_jogos[num_jogo_alterar -1]
        status_jogo = jogo_selecionado.atualizar_status()
    else:
        print('Jogo inválido!')
    
    print(f'O jogo {jogo_selecionado.nome} agora está {jogo_selecionado.obter_status()}')

    continuar = input('Deseja continuar? [S/N]: ')
    if continuar.upper() == 'N':
        break