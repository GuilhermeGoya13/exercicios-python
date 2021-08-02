# Informa a soma, multiplicação, divisão, divisão inteira e potẽncia dos números informados

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma de {} e {} é {}, a multiplicação é {} e a divisão é {:.3f}.'.format(n1, n2, s, m, d), end=' ')
print('Já a divisão inteira é {} e a potência é {}'.format(di, e))
