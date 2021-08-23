'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores.'''

soma = media = c = maior = menor = 0
a = False
while not a:
    n = int(input('Digite um valor: '))
    soma += n
    if c == 1:
        maior = menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    i = str(input('Quer continuar? [S/N] ')).strip()[0]
    if i in 'Ss':
        a = False
        n = int(input('Digite um valor: '))
        c += 1
    elif i in 'Nn':
        a = True
media = soma / c
print('Você inseriu {} números, o maior foi {} e o menor foi {}'.format(c, maior, menor))
print('A média entre eles foi {:.2f}'.format(media))
