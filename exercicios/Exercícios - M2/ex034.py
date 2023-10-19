print('='*30)
print('   PROGRESSÃO ARITIMÉTICA   ')
print('='*30)
p1 = int(input('Primeiro número: '))
r = int(input('Razão: '))
décimo = p1 + (11 - 1) * r
for c in range(p1, décimo, r):
    print('\033[33m{}'.format(c), end=' → ')
print('Fim!\033[m')
