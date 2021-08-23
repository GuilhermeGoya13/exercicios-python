'''Crie um programa que faça o computador jogar Jokenpô com você.
Minha Versão'''

from random import choice
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
escolha = ('pedra', 'papel', 'tesoura')
pc = choice(escolha)
jogador = int(input())
if 1 <= jogador <= 3:
    if jogador == 1:
        jogador = 'pedra'
    elif jogador == 2:
        jogador = 'papel'
    else:
        jogador = 'tesoura'
    print('{}JO{}'.format(cores['amarelo'], cores['limpa']))
    sleep(1)
    print('{}KEN{}'.format(cores['roxo'], cores['limpa']))
    sleep(1)
    print('{}PÔ{}'.format(cores['vermelho'], cores['limpa']))
    sleep(1)
    print('{}{}{} x {}{}{}'.format('\33[1m', jogador, cores['limpa'], '\33[1m', pc, cores['limpa']))
    if jogador == 'pedra' and pc == 'papel' or jogador == 'papel' and pc =='tesoura' or jogador == 'tesoura' and pc == 'pedra':
        print('{}Você perdeu{}'.format(cores['vermelho'], cores['limpa']))
    elif pc == 'pedra' and jogador == 'papel' or pc == 'papel' and jogador =='tesoura' or pc == 'tesoura' and jogador == 'pedra':
        print('{}Você venceu!{}'.format(cores['azul'], cores['limpa']))
    else:
        print('{}Deu um impate!{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('Escolha não definida')
