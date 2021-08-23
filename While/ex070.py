'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

s = c = cont = barato = 0
nomebarato = ' '
while True:
    nome = str(input('Produto: ')).capitalize().strip()
    preco = float(input('Preço: R$'))
    cont += 1
    s += preco
    if preco > 1000:
        c += 1
    if cont == 1 or preco < barato:
        barato = preco
        nomebarato = nome
        barato = preco
    a = str(input('Quer continuar? [S/N] ')).strip()[0]
    while a not in 'SsNn':
        a = str(input('Digite novamente: [S/N] ')).strip()[0]
    if a in 'Nn':
        break
print(f'O total da compra foi R${s:.2f}')
print(f'Temos {c} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${barato:.2f}')
