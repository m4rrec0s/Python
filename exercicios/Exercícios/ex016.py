from datetime import date

n = int(input('Digite seu ano (clique 0 para conferir o ano atual): '))

if n == 0:
    n = date.today().year

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(f'{n} É BISSEXTO')
else:
    print(f'{n} NÂO É BISSEXTO')