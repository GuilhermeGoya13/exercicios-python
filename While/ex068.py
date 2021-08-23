'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
impar = perdeu = par = c = 0
print('-=' * 12 + '-')
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 12 + '-')
while True:
    pc = randint(0, 10)
    n = int(input('Digite um valor: '))
    i = str(input('Par ou Ímpar? [P/I] '))
    if i in 'Pp':
        par = 1
    elif i in 'Ii':
        impar = 1
    s = pc + n
    if s % 2 == 0:
        j = 'PAR'
        if impar == 1:
            perdeu = True
        elif par == 1:
            perdeu = False
    else:
        j = 'ÍMPAR'
        if impar == 1:
            perdeu = False
        elif par == 1:
            perdeu = True
    if perdeu == False:
        print('-' * 30)
        print(f'Você escolheu {n} e computador {pc}. O total de {s} DEU {j}')
        print('-' * 30)
        print('Você VENCEU')
        print('Vamos jogar novamente...')
        print('-=' * 12 + '-')
        c += 1
    else:
        break
print('-' * 30)
print(f'Você escolheu {n} e computador {pc}. O total de {s} DEU {j}')
print('-' * 30)
print('Você PERDEU')
if c == 1:
    print('Você venceu 1 vez')
elif c > 1:
    print(f'Você venceu {c} vezes')
