# Aqui estão definidas as funções que os jogos foram criados
# Créditos dos Jogos:
# Adivinhação => Aulas do canal Curso em Vídeo
# Par ou Ímpar => Baseado no canal Curso em Vídeo, refatorei e modifiquei para que o usuario escolha se ira jogar de novo ou não
# Jokenpô => Aulas do canal Curso em Vídeo



def adivinhacao():
    from random import randint
    computador = randint(0, 10)
    print('Tudo certo, acabei de pensar no numero...')
    print('Será que você consegue adivinhar qual foi?')
    acertou = False
    palpites = 0
    while not acertou:
        jogador = int(input('Qual é seu palpite? '))
        palpites += 1
        if jogador == computador:
            acertou = True
        else:
            if jogador < computador:
                print('Mais... Tente mais uma vez.')
            elif jogador > computador:
                print('Menos... Tente mais uma vez.')
    print('Acertou com {} tentativas. Parabéns!'.format(palpites))




def par_ou_impar():
    from random import randint

    while True:
        jogador = int(input('Diga um valor: '))
        computador = randint(0, 10)
        total = jogador + computador
        tipo = ' '
        while tipo not in 'PI':
            tipo = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
        print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
        if tipo == 'P':
            if total % 2 == 0:
                print('Você VENCEU!')
                break
            else:
                print('Você PERDEU!')
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('Você VENCEU!')
                break
            else:
                print('Você PERDEU!')
                break


def jokenpo():
    from random import randint
    from time import sleep
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('''Sua opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    jogador = int(input('Qual é a sua jogada? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('-=' * 12)
    print('Computador jogou {}.'.format(itens[computador]))
    print('Jogador jogou {}.'.format(itens[jogador]))
    print('-=' * 12)
    if computador == 0:  # Computador jogou PEDRA
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('JOGADOR VENCE!')
        elif jogador == 2:
            print('COMPUTADOR VENCE!')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 1:  # Computador jogou PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCE!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCE!')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 2:  # Computador jogou TESOURA
        if jogador == 0:
            print('JOGADOR VENCE!')
        elif jogador == 1:
            print('COMPUTADOR VENCE!')
        elif jogador == 2:
            print('EMPATE!')
        else:
            print('JOGADA INVÁLIDA!')


def menu():
    print('|=================================|')
    print('|             JOGOS               |')
    print('|=================================|')
    print('|      [1] - Adivinhação          |')
    print('|      [2] - Par ou Ímpar         |')
    print('|      [3] - Jokenpô              |')
    print('|      [0] - FINALIZAR PROGRAMA   |')
    print('|=================================|')

def funcao_principal():
    from time import sleep

    while True:
        sleep(3)
        print()
        print('Vamos lá...')
        sleep(3)
        print('Escolha uma das opções disponiveis...')
        sleep(3)
        print()
        menu()
        print()
        print('Escolha uma das opções!')
        opcao = int(input('Sua opção: '))
        print()
        if opcao == 1:
            sleep(3)
            print('Bela escolha...')
            sleep(3)
            print('Iremos jogar um jogo de "Adivinhação"... ')
            sleep(3)
            print('Eu irei pensar em um numero entre zero e dez e você terá de adivinhar em que numero eu pensei...')
            sleep(3)
            print('E ao final veremos quantas tentativas voce levou para adivinhar....')
            sleep(3)
            print('Vamos nessa! ')
            adivinhacao()
            print('Deseja jogar novamente?')
            print('[1] - SIM')
            print('[2] - NAO')
            resp = int(input())
            if resp == 1:
                adivinhacao()
                print('Deseja jogar novamente?')
                print('[1] - SIM')
                print('[2] - NAO')
                resp = int(input())
                adivinhacao()
            elif resp == 2:
                funcao_principal()
                break
        elif opcao == 2:
            sleep(3)
            print('Escolha perfeita...')
            sleep(3)
            print('Iremos jogar um jogo chamado de "Par ou Impar"... ')
            sleep(3)
            print('Você irá digitar um numero, e escolher entre par ou impar...')
            sleep(3)
            print('Eu irei sortear um numero aleatorio e ficarei com a outra opção...')
            sleep(3)
            print('Esses numeros serão somados e ganha quem acertar se a soma dos numeros\n'
                  'resultou em Par ou Impar...')
            sleep(3)
            print('Vamos nessa! ')
            sleep(3)
            par_ou_impar()
            print('Deseja jogar novamente?')
            print('[1] - SIM')
            print('[2] - NAO')
            resp = int(input())
            if resp == 1:
                par_ou_impar()
                print('Deseja jogar novamente?')
                print('[1] - SIM')
                print('[2] - NAO')
                resp = int(input())
                par_ou_impar()
            elif resp == 2:
                funcao_principal()
                break
        elif opcao == 3:
            sleep(3)
            print('Show, esse é um dos meus jogos preferidos...')
            sleep(3)
            print('Iremos jogar Jokenpô, ou o clássico Pedra, Papel e Tesoura... ')
            sleep(3)
            print('Só lembrando que:\n'
                  ' Pedra ganha da tesoura (amassando-a ou quebrando-a),\n'
                  'Tesoura ganha do papel (cortando-o),\n'
                  'Papel ganha da pedra (embrulhando-a).')
            sleep(3)
            print('Vamos nessa! ')
            jokenpo()
            print('Deseja jogar novamente?')
            print('[1] - SIM')
            print('[2] - NAO')
            resp = int(input())
            if resp == 1:
                jokenpo()
                print('Deseja jogar novamente?')
                print('[1] - SIM')
                print('[2] - NAO')
                resp = int(input())
                jokenpo()
            elif resp == 2:
                funcao_principal()
                break
        elif opcao == 0:
            sleep(3)
            print('Obrigado por passar esse tempo comigo')
            sleep(3)
            print('Volte sempre que quiser se divertir')
            sleep(3)
            print('FINALIZANDO......')
            break
        else:
            print('<<<<< Opção Inválida! >>>>>')

