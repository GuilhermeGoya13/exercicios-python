'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

n = int(input('Digite um número: '))
p = 0  # contador
for c in range(1, n+1):
    r = n % c
    if c == n:
        print('{}{}{}'.format('\33[32m', c, '\33[m'), end='.')
    else:
        if c == 1 or c == n:
            print('{}{}{}'.format('\33[32m', c, '\33[m'), end=', ')
            p += 1
        elif c != 1 and c != n and r == 0:
            print('{}{}{}'.format('\33[31m', c, '\33[m'), end=', ')
        else:
            print(c, end=', ')
        if c % 27 == 0:
            print('\n')
if p == 2:
    print('\nO número digitado é primo')
else:
    print('\nO número digitado não é primo')
