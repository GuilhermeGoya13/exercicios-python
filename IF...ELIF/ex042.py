'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

from math import sqrt, pow
n1 = float(input('Informe o segmento 1: '))
n2 = float(input('Informe o segmento 2: '))
n3 = float(input('Informe o segmento 3: '))
s1 = n1 + n2
s2 = n1 + n3
s3 = n2 + n3
b1 = sqrt((pow(n1, 2)) + (pow(n2, 2)))
b2 = sqrt((pow(n1, 2)) + (pow(n3, 2)))
b3 = sqrt((pow(n2, 2)) + (pow(n3, 2)))
cores = {'azul': '\33[36m',
         'vermelho': '\33[31m',
         'limpa': '\33[m'}
if b1 == n3 or b2 == n2 or b3 == n1:
    print('É um \33[4;32mTRIÂNGULO RETÂNGULO{}'.format(cores['limpa']))
if s1 > n3 and s2 > n2 and s3 > n1:
    if n1 == n2 == n3:
        print('Estes segmentos podem formar um triângulo {}EQUILÁTERO{}.\n'.format(cores['azul'], cores['limpa']))
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print('Estes segmentos podem formar um triângulo {}ISÓSCELES{}'.format(cores['azul'], cores['limpa']))
    else:
        print('Estes segmentos podem formar um triângulo {}ESCALENO{}'.format(cores['azul'], cores['limpa']))
else:
    print('{}Estes segmentos não podem formar um triângulo{}'.format(cores['vermelho'], cores['limpa']))
