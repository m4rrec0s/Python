def soma(a, b):
    print(f'A = {a} B = {b}')
    s = a + b
    print(f'A soma vale {s}')
    print('-'*30)

while True:
    op = ''
    a = int(input('Num 1:'))
    b = int(input('Num 2: '))
    soma(a, b)
    op = str(input('Quer continuar? '))
    if op in 'Nn':
        break
print('<< FIM >>')
