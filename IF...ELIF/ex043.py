'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
 seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

peso = float(input('Informe o seu peso em Kg: '))
altura = float(input('Informe a sua altura em metro: '))
imc = peso / (altura ** 2)
cores = {'azul': '\33[36m',
         'roxo': '\33[35m',
         'vermelho': '\33[31m',
         'vermelho2': '\33[1;31m',
         'limpa': '\33[m'}
if imc < 18.5:
    print('O seu IMC é {:.1f}'.format(imc))
    print('{}Abaixo do peso{}'.format(cores['roxo'], cores['limpa']))
elif 18.5 <= imc < 25:
    print('O seu IMC é {:.1f}'.format(imc))
    print('{}Peso ideal{}'.format(cores['azul'], cores['limpa']))
elif 25 <= imc < 30:
    print('O seu IMC é {:.1f}'.format(imc))
    print('\33[1mSobrepeso{}'.format(cores['limpa']))
elif 30 <= imc < 40:
    print('O seu IMC é {:.1f}'.format(imc))
    print('{}Obesidade{}'.format(cores['vermelho'], cores['limpa']))
else:
    print('O seu IMC é {:.1f}'.format(imc))
    print('{}Obesidade mórbida{}'.format(cores['vermelho2'], cores['limpa']))
