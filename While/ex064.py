'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''

c = soma = 0
n = int(input(f'Digite o 1º valor: '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite o {}º valor: '.format(c+1)))
print('A soma de todos os {} números é {}'.format(c, soma))
