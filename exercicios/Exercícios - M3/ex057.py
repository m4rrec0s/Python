from random import randint
numeros = (randint(0,10), randint(0,10),
           randint(0,10),randint(0,10),
           randint(0,10))
print(f'os numeros sorteados foram {numeros}')
print(f'o maior foi {max(numeros)}')
print(f'o menor foi {min(numeros)}')
