matriz = [[], [], []]
numeros = []
l = c = 0
for n in range(9):
    linha = int(input(f'Digite a posição [{l}, {c}]: '))
    numeros.append(linha)
    matriz[l].append(numeros[:])
    numeros.clear()

    c += 1

    if len(matriz[0]) == 3:
        l = 1
    if len(matriz[1]) == 3:
        l = 2
    if c == 3:
        c = 0

print('')
print('—'*30)
print(f'{"MATRIS":^30}|')
print(f'{matriz[0]}', end='')
print(f'\n{matriz[1]}', end='')
print(f'\n{matriz[2]}', end='')
print('')
print('—'*30)
