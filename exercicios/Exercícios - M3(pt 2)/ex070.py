matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = mai = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l}, {c}]: '))
print('--' * 30)

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] %2 ==0:
            spar += matriz[l][c]
    print()
print('--' * 30)
# CALCULOS
print(f'A soma dos valores pares é {spar}')
for l in range(3):
    scol += matriz[l][2]
print(f'A soma dos valores da 3º coluna é {scol}')
print(f'O maior valor da 2ª linha é {max(matriz[1])}')
print('--' * 30)
