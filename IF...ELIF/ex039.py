'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
 alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
 também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano = int(input('Informe o seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    f = 18 - idade
    if f == 1:
        print('\33[36mVocê tem {} anos, então ainda falta 1 ano para você ter que se alistar.\33[m'.format(idade))
        data = date.today().year + f
        print('Você se alistará em {}'.format(data))
    else:
        print('\33[36mVocê tem {} anos, então ainda faltam {} anos para você ter que se alistar\33[m'.format(idade, f))
        data = date.today().year + f
        print('Você se alistará em {}'.format(data))
elif idade == 18:
    print('\33[31mVocê já tem 18 anos, então precisa se alistar com urgência!\33[31m')
else:
    f = idade - 18
    if f == 1:
        print('\33[36mVocê já tem {} anos, então você já deve ter se alistado há 1 ano atrás\33[m'.format(idade))
        data = date.today().year - f
        print('Você se alistou em {}'.format(data))
    else:
        print('\33[36mVocê já tem {} anos, então você já deve ter se alistado há {} anos atrás\33[m'.format(idade, f))
        data = date.today().year - f
        print('Você se alistou em {}'.format(data))
