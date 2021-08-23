'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o
salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o
empréstimo será negado.'''

from math import ceil
preço = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o valor do seu salário? R$'))
'''mes = ano * 12
parcela = preço / mes
porcento = salario * 0.3'''

tempo = (preço / (salario * 3.6))

if tempo <= 1:
    print('\nVocê pode financiar a casa em no minímo 1 ano')
    meses = ceil(tempo * 12)
    print('Em um total de {} meses'.format(meses))
else:
    print('\nVocê pode financiar em no minímo {} anos.\n'.format(tempo))
ano = int(input('Em quantos anos você pretende pagar o financiamento? '))

'''if parcela < porcento:
    print('\33[36mTudo certo para o seu financiamento!\33[m')
else:
    print('\33[31mInfelizmente não será possivel fazer este financiamento.\33[m')'''

if ano >= tempo:
    parcela = preço / (ano * 12)
    print('\33[36mTudo certo, você pagará em até {} anos e os valores mensais serão {:.2f}.\33[m'.format(ano, parcela))
else:
    print('\33[31mInflizmente não podemos financiar em tão pouco tempo.\33[m')
