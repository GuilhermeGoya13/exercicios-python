# Mostra o primeiro e o último nome da pessoa

nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
primeiro = dividido[0]
ultimo = dividido[len(dividido) - 1]
print('{} {}'.format(primeiro, ultimo))
