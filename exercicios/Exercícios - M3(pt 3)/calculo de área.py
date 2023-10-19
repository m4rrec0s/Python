from time import sleep

def calcular_área(a, b):
    s = a * b
    print('-'*30)
    print('calculando...')
    sleep(1)
    print(f'A = {a}m x {b}m\nA = {s}m²')
    print ('-' * 30)

a = int(input('Base: '))
b = int(input('Altura: '))

calcular_área(a, b)
