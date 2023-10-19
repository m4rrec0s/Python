import time

time.sleep(1)
print('''TABELA DE SALÁRIOS
ATÉ R$ 1200.00 - AUMENTO DE 15%
ACIMA DE R$ 1200.00 - AUMENTO DE 10%''')

print(' ')
time.sleep(1.5)

n = int(input('De quanto é o seu salário? R$ '))
a = (n * (15/100) + n)
b = (n * (10/100) + n)

time.sleep(2)
if n <= 1200:
    print('SEU SALÁRIO VAI DE R$ {} PARA R$ {}'.format(n, a))
    time.sleep(2)
else:
    print('SEU SALÁRIO VAI DE R$ {} PARA {}'.format(n, b))
    time.sleep(2)
