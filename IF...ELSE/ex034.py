# Informa o aumento do salário

salario = float(input('Digite o valor do seu salario: '))
if salario >= 1250:
    print('Seu salário será de {} reais'.format(salario*0.1+salario))
else:
    print('Seu salário será de {} reais'.format(salario*0.15+salario))
