# Informa se as retas inseridas conseguem formar um triângulo

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

s1 = r1 + r2
s2 = r1 + r3
s3 = r2 + r3

if s1 > r3 and s2 > r2 and s3 > r1:
    print('Estas retas conseguem formar um triângulo')
else:
    print('ERRO!')
'''if s1 > r3:
    if s2 > r2:
        if s3 > r1:
            print('Estas retas conseguem formar um triângulo')
        else:
            print('ERRO!')
    else:
        print('ERRO!')
else:
    print('ERRO!')'''
