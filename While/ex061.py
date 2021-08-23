'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while.'''

n = int(input('Informe o primeiro valor: '))
r = int(input('Informe a razão: '))
'''c = 2
print(f'{n}', end=' ')
while c <= 10:
    pa = n + r
    n = pa
    print(pa, end=' ')
    c += 1
print('FIM')'''

termo = n
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')

'''for c in range(1, 10):
    pa = n + r
    n = pa
    print(pa, end=' ')
print('FIM')'''
