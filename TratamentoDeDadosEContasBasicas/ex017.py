# Encontra a hipotenusa pelos catetos

from math import sqrt, pow, hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
'''hip = ((co ** 2) + (ca ** 2)) ** (1/2)'''
'''hip = sqrt(pow(co, 2) + pow(ca, 2))'''
hip = hypot(co, ca)
print('A hipotenusa desse triangulo retângulo vale {:.2f}'.format(hip))
