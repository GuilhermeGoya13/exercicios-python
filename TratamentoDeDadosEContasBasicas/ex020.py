# Sorteia a ordem dos grupos

from random import shuffle
n1 = str(input('Nome 1: '))
n2 = str(input('Nome 2: '))
n3 = str(input('Nome 3: '))
n4 = str(input('Nome 4: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(lista)
