# Informa o custo da viagem de acordo com a distância

n = float(input('Qual a distância da viagem? '))
# if n <= 200:
#     print('A viagem custará R${:.2f}'.format(n*0.5))
# else:
#     print('A viagem custará R${:.2f}'.format(n*0.45))
preço = n * 0.5 if n <= 200 else n * 0.45
print('A viagem custará R${:.2f}'.format(preço))
