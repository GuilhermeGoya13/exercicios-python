'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo
de 1 até 500.'''

print('A soma dos números ímpares, múltiplos de 3 e entre 1 e 500 é: ')
s = 0
cont = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        s += c
        cont += 1
print('{} e foram {} números'.format(s, cont))
print('FIM')
