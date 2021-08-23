'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''

from datetime import date
ano = int(input('Informe a data de nascimento do atleta: '))
idade = date.today().year - ano
'''if ano < date.today().year:
    if idade <= 9:
        print('O atleta tem {} anos'.format(idade))
        print('Classificação: MIRIM')
    elif 9 < idade <= 14:
        print('O atleta tem {} anos'.format(idade))
        print('Classificação: INFANTIL')
    elif 14 < idade <= 19:
        print('O atleta tem {} anos'.format(idade))
        print('Classificação: JUNIOR')
    elif 19 < idade <= 20:
        print('O atleta tem {} anos'.format(idade))
        print('Classificação: SÊNIOR')
    else:
        print('O atleta tem {} anos'.format(idade))
        print('Classificação: MASTER')'''
if ano < date.today().year:
    if idade <= 9:
        print('O atleta tem {} anos'.format(idade))
        print('Classificação: MIRIM')
    elif idade <= 14:
        print('O atleta tem {} anos'.format(idade))
        print('Classificação: INFANTIL')
    elif idade <= 19:
        print('O atleta tem {} anos'.format(idade))
        print('Classificação: JUNIOR')
    elif idade <= 20:
        print('O atleta tem {} anos'.format(idade))
        print('Classificação: SÊNIOR')
    else:
        print('O atleta tem {} anos'.format(idade))
        print('Classificação: MASTER')
else:
    print('DATA INVÁLIDA')
