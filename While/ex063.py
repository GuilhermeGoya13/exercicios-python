'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''

n = int(input('Digite a quantia de números a serem mostrados na sequencia de fibonacci: '))
c = 3  # contador
g = 1  # atualizador de dado
i = 0  # atualizador de dado
f = 1  # número de fibonacci
print('0 ->', end=' ')
while c <= n:
    print(f, end=' -> ')
    f = g + i
    i = g
    g = f
    c += 1
print(f)
