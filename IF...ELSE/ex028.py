# Adivinha o número que o jogador pensou

from random import randint
from time import sleep  # importa o sleep da biblioteca time para poder fazer a pausa de 1 segundo
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
computador = randint(0, 5)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)  # cria uma pausa de 1 segundo
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
