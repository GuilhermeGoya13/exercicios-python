'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

n = int(input('Digite um número: '))
for c in range(1, 11):
    r = n * c
    print('{} * {} = {}'.format(n, c, r))
print('FIM')
