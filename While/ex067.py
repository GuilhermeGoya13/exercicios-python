'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
programa será interrompido quando o número solicitado for negativo.'''

while True:
    n = int(input('Qual tabuada você quer ver? '))
    if n < 0:
        break
    print('-'*29)
    for c in range(1, 11):
        t = n * c
        print(f'{n} * {c} = {t}')
    print('-'*29)
