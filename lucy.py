from time import sleep


def lucy_apresentacao():
    sleep(2)
    print()
    print()
    print('<<<<<     CARREGANDO     >>>>>  ')
    print()
    sleep(3)
    print('Olá, me chamo Lucy, seja bem vindo ao meu ambiente virtual... ')
    sleep(3)
    print('Para que possamos ter uma experiência agradavel me diga um pouco sobre você... ')
    sleep(3)
    usuario_apresentacao()




def usuario_apresentacao():

    print('Tudo bem, vamos lá me diga seu nome...')
    nome = input('>> ').title()
    print(f'Legal, {nome}!')
    sleep(3)
    print('De que cidade você é? ')
    cidade = input('>> ').title()
    print(f'{cidade}, interesssante. Mas {nome}, em que Estado fica essa cidade? ')
    sleep(3)
    estado = input('>> ').title()
    print(f'Ah sim.  {estado} é um Estado maravilhoso, povo muito acolhedor... ')
    sleep(3)
    print('O que voce curte fazer no seu tempo livre? ')
    hobbies = input('>> ')
    print(f'Entendi. Seus hobbies entao são {hobbies}...')
    sleep(3)
    print(f'{nome}, quero lhe levar a uma experiencia atraves do mundo do jogos...')
    sleep(3)
    print('É só você escolher uma das opções e se divertir...')
    sleep(3)
    print('E desde já agradeço por sua companhia...')


