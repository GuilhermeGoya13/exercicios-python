# Informa quantas vezes a letra A aparece na frase, a primeira posição e a ultima

frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A letra A aparece pela primeira vez no espaço {}'.format(frase.find('a')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('a')+1))
