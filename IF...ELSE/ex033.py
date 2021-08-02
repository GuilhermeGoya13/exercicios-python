# Informa o menor e o maior número digitado

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
'''if n1 > n2:
    if n1 > n3:
        maior = n1
else:
    if n1 < n3:
        menor = n1
if n2 > n3:
    if n2 > n1:
        maior = n2
else:
    if n2 < n1:
        menor = n2
if n3 > n1:
    if n3 > n2:
        maior = n3
else:
    if n3 < n2:
        menor = n3'''
print('O maior número é {}\nO menor número é {}'.format(maior, menor))
