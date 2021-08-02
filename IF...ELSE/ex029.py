# Informa o valor da multa baseada na velocidade

from math import trunc
v = float(input('Digite a velocidade do carro: '))
if v > 80:
    print('Você está acima do limite de velocidade! Você receberá uma multa no valor de {} reais'.format(trunc((v-80))*7))
else:
    print('Dirija com cuidado!')
