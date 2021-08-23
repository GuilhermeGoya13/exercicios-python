'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
c = 1
t = 0
print('-='*28 + '-')
print("Vou pensar em um número entre 1 e 10. Tente adivinhar...")
print('-='*28 + '-')
pc = randint(1, 10)
n = int(input('Adivinhe o número em que eu pensei: '))
'''acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')'''
while n != pc:
    if 0 < n < 11:
        print('{}ERROU!!{}'.format('\33[31m', '\33[m'))
        if pc > n:
            print('Um pouco mais...')
        else:
            print('Um pouco menos...')
        c += 1
    else:
        print('Esse número está fora do alcance em que eu pensei')
        t += 1
    n = int(input('Adivinhe o número em que eu pensei: '))
print('{}Você acertou na {}ª tentativa, mas você colocou {} vezes números errados, totalizando {} tentativas totais!{} \nEu pensei no número {}'.format('\33[32m', c, t, c+t, '\33[m', pc))
