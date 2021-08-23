'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
 pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''

preço = float(input('Digite o valor do produto: '))
cores = {'azul': '\33[4;36m',
         'roxo': '\33[4;35m',
         'vermelho': '\33[4;31m',
         'amarelo': '\33[4;33m',
         'limpa': '\33[m'}
#pagamento = {'', 'dinheiro/cheque', 'a vista cartão', 'cartão <= 2x', 'cartão > 3x'}
print('Informe a forma de pagamento')
print('{}À vista no dinheiro/cartão{} (1)'.format(cores['azul'], cores['limpa']))
print('{}À vista no cartão{} (2)'.format(cores['roxo'], cores['limpa']))
print('{}Em até 2x no cartão{} (3)'.format(cores['vermelho'], cores['limpa']))
print('{}Em 3x ou mais no cartão{} (4)'.format(cores['amarelo'], cores['limpa']))
a = int(input())
if a == 1:
    print('Você escolheu à vista no dinheiro/cartão, recebendo 10% de desconto')
    novo = preço * 0.9
    print('Seu produto sairá com o valor de R${:.2f}'.format(novo))
elif a == 2:
    print('Você escolheu à vista no cartão, recebendo 5% de desconto')
    novo = preço * 0.95
    print('Seu produto sairá com o valor de R${:.2f}'.format(novo))
elif a == 3:
    print('Você escolheu em até 2x no cartão')
    print('O preço será R${:.2f}'.format(preço))
elif a == 4:
    novo = preço * 1.2
    print('Você escolheu pagar em 3x ou mais no cartão, haverá 20% de juros. O valor atual é de R${:.2f}'.format(novo))
    q = int(input('Em quantas vezes você pretende parcelar (máximo 12)? '))
    if q <= 12:
        pag = novo / q
        print('Você parcelará em {}x, cada parcela sairá no valor de R${:.2f}'.format(q, pag))
    else:
        print('Quantia inválida')
else:
    print('\33[31mRESPOSTA INVÁLIDA{}'.format(cores['limpa']))
