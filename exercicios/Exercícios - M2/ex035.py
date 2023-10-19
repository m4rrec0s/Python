n1 = int(input('Digite um número: '))

s = 0
#ct = 0
for c in range(1, n1 + 1):
    #ct += s
    if n1 % c == 0:
        print('\033[33m', end='')
        s += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi dividido {} vezes.'.format(n1, s))

if s > 2:
    print('Por isso ele não é PRIMO.')
else:
    print('Por isso ele PRIMO')
