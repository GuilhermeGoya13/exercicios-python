'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
 digitado for ímpar, desconsidere-o.'''

s = 0
for c in range(0, 6):
    n = int(input('Digite o {}º número: '.format(c+1)))
    r = n % 2
    if r == 0:
        s += n
if s == 0:
    print('Não houve nenhum número par')
else:
    print('A soma dos números pares é {}'.format(s))
