'''Crie um programa que faça o computador jogar Jokenpô com você.
Versão do Professor'''

from random import randint
from time import sleep
cores = {'azul': '\33[34m',
         'roxo': '\33[35m',
         'amarelo': '\33[33m',
         'vermelho': '\33[31m',
         'limpa': '\33[m'}
print('-='*15+'-')
print('{}{:^31}{}'.format(cores['roxo'], 'JOKENPÔ', cores['limpa']))
print('-='*15+'-')
print('{:^31}\n{}PEDRA{}  {}PAPEL{}   {}TESOURA{}'.format('Faça sua escolha', '\33[1m', cores['limpa'], '\33[1m', cores['limpa'], '\33[1m', cores['limpa']))
print(' (1)    (2)      (3)')
escolha = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
jogador = int(input())
jogador = jogador - 1
if 0 <= jogador <= 2:
    print('{}JO{}'.format(cores['amarelo'], cores['limpa']))
    sleep(1)
    print('{}KEN{}'.format(cores['roxo'], cores['limpa']))
    sleep(1)
    print('{}PÔ{}'.format(cores['vermelho'], cores['limpa']))
    sleep(1)
    print('{}{}{} x {}{}{}'.format('\33[1m', escolha[jogador], cores['limpa'], '\33[1m', escolha[pc], cores['limpa']))
    if jogador == 0:
            if pc == 0:
                print('{}Deu um impate!{}'.format(cores['amarelo'], cores['limpa']))
            elif pc == 1:
                print('{}Você perdeu{}'.format(cores['vermelho'], cores['limpa']))
            else:
                print('{}Você venceu!{}'.format(cores['azul'], cores['limpa']))
    elif jogador == 1:
        if pc == 0:
            print('{}Você venceu!{}'.format(cores['azul'], cores['limpa']))
        elif pc == 1:
            print('{}Deu um impate!{}'.format(cores['amarelo'], cores['limpa']))
        else:
            print('{}Você perdeu{}'.format(cores['vermelho'], cores['limpa']))
    elif jogador == 2:
        if pc == 0:
            print('{}Você perdeu{}'.format(cores['vermelho'], cores['limpa']))
        elif pc == 1:
            print('{}Você venceu!{}'.format(cores['azul'], cores['limpa']))
        else:
            print('{}Deu um impate!{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('Escolha não definida')
