# Mostra um nome escrito em caixa alta, caixa baixa, o total de letras e o total de letras do primeiro nome

nome = str(input('Digite o seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
dividido = nome.split()
juntar = ''.join(dividido)
print(len(juntar))
# print(len(nome) - nome.count(' '))
print(len(dividido[0]))
# print(nome.find(' '))
