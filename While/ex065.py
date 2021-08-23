'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores.'''

soma = maior = menor = 0
c = 1
a = False
while not a:
    n = int(input('Digite o {}º valor (digite 0 para sair): '.format(c)))
    if c == 1:
        maior = menor = n
    soma += n
    if n != 0:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
        c += 1
    if n == 0:
        r = str(input('Gostaria de acrescentar algum valor? [S/N] '))
        while r not in 'SsNn':
            r = str(input('RESPOSTA INVÁLIDA! INFORME NOVAMENTE [S/N] '))
        if r in 'Ss':
            n = int(input('Digite o {}º valor: '.format(c)))
            soma += n
            if n != 0:
                if n > maior:
                    maior = n
                elif n < menor:
                    menor = n
                c += 1
        elif r in 'Nn':
            a = True
            c -= 1
media = soma / c
if c == 1:
    print('Você digitou 1 número')
    print('A média é o próprio valor e não houve menor ou maior')
else:
    print('Você digitou {} números'.format(c))
    print('A média é {:.2f}'.format(media))
    if maior == menor:
        print('Não houve maior ou menor número')
    else:
        print('O maior número inserido foi {}'.format(maior))
        print('O menor número inserido foi {}'.format(menor))
