'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

n = float(input('Digite o 1º peso em Kg: '))
menor = n
maior = n
for c in range(2, 6):
    n = float(input('Digite o {}º peso em Kg: '.format(c)))
    if n < menor:
        menor = n
    if n > maior:
        maior = n
print('O maior peso é {:.2f}Kg e o menor peso é {:.2f}Kg'.format(maior, menor))
