# Calcula a área de uma parede e informa quantos litros de tinta serão necessários para pintar a parede

n1 = float(input('Qual a altura da parede? '))
n2 = float(input('Qual a largura da parede? '))
a = n1 * n2
t = a / 2
print('Para pintar esta parede serão necessarios {} litros de tinta'.format(t))
