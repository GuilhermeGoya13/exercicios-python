# Informa a unidade, dezena, centena e milhar de um número

num = int(input('Digite um número entre 0 e 9999: '))
a = num // 1 % 10
b = num // 10 % 10
c = num // 100 % 10
d = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(a))
print('Dezena: {}'.format(b))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(d))
