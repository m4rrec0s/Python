from random import randint
from time import sleep

numeros = [[], []]

def sorteio():
    for c in range(5):
        numeros[0].append(randint(1, 10))

def somaPar(lista):
    soma = 0
    for n in lista:
        if n %2 == 0:
            soma += n
    print(soma)

print('-'*40)
print(f'Sorteando 5 valores: ', end='')
sorteio()
for d in numeros[0]:
    print(d, end=' ')
    sleep(0.5)
print('Pronto!')

print(f'Somando os valores pares, temos: ', end='')
sleep(0.5)
somaPar(numeros[0])
print('-'*40)
