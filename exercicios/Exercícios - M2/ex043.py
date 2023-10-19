num = int(input('Digite um número: '))
c = num
resultado = 1
print('{}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    resultado *= c
    c -= 1
print(resultado)

# =============== SEGUNDA PARTE =================== #

num2 = int(input('Digite um número: '))
s = 0
resultado2 = 1
for i in range(num2, 0, -1):
    resultado2 *= i
print(resultado2)
#print('{}! = {} = {}'.format(num2, i, resultado2, end= ''))

