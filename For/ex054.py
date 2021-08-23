'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.'''

from datetime import date
ano = date.today().year  # usa o ano na configurção do PC
b = 0  # contador das pessoas maiores de idade
m = 0  # contador das pessoas menores de idade
for c in range(0, 7):
    n = int(input('Digite o ano de nascimento: '))
    a = ano - n  # calcula a idade da pessoa
    if a >= 18:
        b += 1
    else:
        m += 1
print('A número de pessoas maiores de idade é {}'.format(b))
print('O número de pessoas menores de idade é {}'.format(m))
print('FIM')
