print('~'*45)
n = int(input('      Quantos termos você quer ver? '))
print('~'*45)
t1 = 0
t2 = 1
print('{} → {} '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t2 + t1
    print('→ {}'.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print(' → FIM')
print('~'*45)
