'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
b = False
while not b:
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] Sair do programa\n')
    a = int(input())
    while a <= 0 or a > 5:
        print('\nOPÇÃO INVÁLIDA!\n')
        a = int(input())
    if a == 1:
        soma = n1 + n2
        print('\nA soma entre {} e {} é {}\n'.format(n1, n2, soma))
    elif a == 2:
        multiplicar = n1 * n2
        print('\nA multiplicação entre {} e {} é {}\n'.format(n1, n2, multiplicar))
    elif a == 3:
        if n1 < n2:
            print('\n{} é maior que {}\n'.format(n2, n1))
        elif n1 > n2:
            print('\n{} é maior que {}\n'.format(n1, n2))
        else:
            print('\nAmbos tem o mesmo valor\n')
    elif a == 4:
        print('\n')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    else:
        b = True
print('\nFIM')
