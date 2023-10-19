lista = []
maior = menor = 0
for cont in range(0,5):
    lista.append(int(input(f'Digite um número na posição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]

print(f'Você digitou os valores {lista}')
print('-'*30)
print(f'O maior valor é {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor é {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')

print('\nFim')
