'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
ele disser que quer mostrar 0 termos.'''

n = int(input('Informe o primeiro valor: '))
r = int(input('Informe a razão: '))
c = 2  # contador
i = n  # atualiza os valores da pa
s = 10  # limite do contador
print(n, end=' ')
while c <= s:
    pa = i + r
    i = pa
    print(pa, end=' ')
    c += 1
a = int(input('\nGostaria de adicionar mais termos à sua PA? (digite 0 para sair) '))
if a <= 0:
    print('FIM')
while a > 0:
    c = 2
    i = n
    print(n, end=' ')
    s = s + a
    while c <= s:
        pa = i + r
        i = pa
        print(pa, end=' ')
        c += 1
    a = int(input('\nGostaria de adicionar mais termos à sua PA? (digite 0 para sair) '))
print('Progressão finalizada com {} termos mostrados'.format(s))
print('FIM')
