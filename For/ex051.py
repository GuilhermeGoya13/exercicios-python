'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.'''

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.: '))
for c in range(1, 11):
    p = n + (c - 1) * r
    print(p, end=', ')
print('\nFIM')
