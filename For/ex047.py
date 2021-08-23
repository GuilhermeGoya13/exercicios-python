'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

print('O números pares de 1 a 50 são: ')
cores = {'1': '\33[32m',
         '2': '\33[33m',
         '3': '\33[34m'}
#while cores <= 4:
#   if cores == 4:
#      cores == 1
for c in range(0, 50, 2):
    print('\33[32m', c+2, '\33[m', end=' ')
# cores += 1
print('FIM')
