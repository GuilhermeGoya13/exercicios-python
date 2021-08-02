# Informa o valor a ser pago por um carro alugado pela quilometragem rodada e dia alugado

d = int(input('Quantos dias alugado? '))
km = int(input('Quantos km percorridos? '))
print('O total a ser pago pelo carro são {} reais'.format((d*60)+(km*0.15)))
