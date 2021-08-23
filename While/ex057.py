'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
digitação novamente até ter um valor correto.'''

sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('DADOS INVÁLIDOS!')
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
if sexo in 'M':
    print('Sexo Masculino')
else:
    print('Sexo Feminino')
print('FIM')
