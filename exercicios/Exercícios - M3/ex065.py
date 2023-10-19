numeros = []
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    opcao = str(input('Deseja adcionar outro valor? [S/N] '))
    if opcao in 'Nn':
        break

pares = []
impares = []

for d, c in enumerate(numeros):
    if c %2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print('-'*30)
print(f'LISTA COMPLETA: {numeros}')
pares.sort()
print(f'PARES: {pares}')
impares.sort()
print(f'IMPARES: {impares}')
