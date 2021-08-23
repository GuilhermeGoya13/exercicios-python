'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

soma = 0
velho = 0  # declara a variavel para armazenar a idade do homem mais velho
nomevelho = ''  # declara a variavel para armazenar o nome do homem mais velho
i = 0  # soma das mulheres com menos de 20 anos
for c in range(1, 5):
    print('-'*5, f'{c}ª PESSOA', '-'*5)
    nome = str(input('Nome: ')).capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if sexo in 'Mm':
        velho = idade
        nomevelho = nome
        if idade > velho:
            velho = idade
            nomevelho = nome
    elif sexo in 'Ff':
        if idade < 20:
            i += 1
media = soma / c
print('A média das idades é de {:.1f} anos'.format(media))
print('O homem mais velho é {} com {} anos'.format(nomevelho, velho))
print('A quantidade de mulheres com menos de 20 anos é de {}'.format(i))
