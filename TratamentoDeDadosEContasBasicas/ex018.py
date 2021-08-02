# Informa o seno, cosseno e tangente de um ânbgulo

from math import sin, cos, tan, radians
t = float(input('Digite o valor do ângulo: '))
rad = radians(t)
se = sin(rad)
co = cos(rad)
ta = tan(rad)
print('O seno, cosseno e tangente desse ângulo são {:.2f}, {:.2f} e {:.2f}'.format(se, co, ta))
