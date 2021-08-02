# Informa se o ano é bissexto

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
ms = 'O ano de {} é bissexto'.format(ano)
mn = 'O ano de {} não é bissexto'.format(ano)
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(ms)
        else:
            print(mn)
    else:
        print(ms)
else:
    print(mn)
