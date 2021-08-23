'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
Minha versão'''

c = v = d = u = cont = 0
print('-='*10 + '-')
print('{:^21}'.format('Caixa Eletrônico'))
print('-='*10 + '-')
valor = int(input('Digite o valor a ser sacado: '))
for i in range(valor, 0, -1):
    cont += 1
    u += 1
    if cont % 50 == 0:
        c += 1
        v -= 2
        u -= 10
        cont -= 50
    elif cont % 20 == 0:
        v += 1
        d -= 1
        u -= 10
    elif cont % 10 == 0:
        d += 1
        u -= 10
if c != 0:
    print(f'Total de {c} cédulas de R$50')
if v != 0:
    print(f'Total de {v} cédulas de R$20')
if d != 0:
    print(f'Total de {d} cédulas de R$10')
if u != 0:
    print(f'Total de {u} cédulas R$1')
