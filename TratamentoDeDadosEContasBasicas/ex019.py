# Sorteia um aluno para apagar a lousa

from random import choice
n1 = str(input('Nome 1: '))
n2 = str(input('Nome 2: '))
n3 = str(input('Nome 3: '))
n4 = str(input('Nome 4: '))
lista = [n1, n2, n3, n4]
#print('O aluno que irá apagar o quadro será: {}'.format(choice(n1, n2, n3, n4)))
print('O aluno que irá apagar o quadro será: {}'.format(choice(lista)))
