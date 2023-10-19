#VALOR INTEIRO
from math import trunc, sqrt
num = float(input('Digite um numero quebrado: '))
print('O valor inteiro é {}.'.format(trunc(num)))
print('='*20)
print('Calculando uma hipotenuza de um triângulo retângulo:')
num2 = int(input('-> cateto 1: '))
num3 = int(input('-> cateto 2: '))
r = sqrt(num2 ** 2 + num3 ** 2)
print('O valor da hipotenuza é {}'.format(trunc(r)))
