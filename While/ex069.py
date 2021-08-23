'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

c = h = m = 0
a = ' '
while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    n = int(input('Idade: '))
    if n >= 18:
        c += 1
    sexo = ' '
    while sexo not in 'MmFf':
        i = str(input('Sexo: [M/F] ')).strip()[0]
    if i in 'Mm':
        h += 1
    elif i in 'Ff':
        if n < 20:
            m += 1
    print('-' * 30)
    a = str(input('Quer continuar: [S/N] '))
    while a not in 'SsNn':
        a = str(input('Digite novament: [S/N] ')).strip()[0]
    if a in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {c}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {m} mulheres com menos de 20 anos')
