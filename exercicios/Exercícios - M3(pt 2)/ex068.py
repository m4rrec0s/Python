numeros = [[], []]
valor = 0
for n in range(7):
    valor = int(input(f'Digite o {n+1}° valor: '))
    if valor %2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-'*30)
numeros[0].sort()
numeros[1].sort()
print(f'PARES: {numeros[0]}')
print(f'IMPARES: {numeros[1]}')
