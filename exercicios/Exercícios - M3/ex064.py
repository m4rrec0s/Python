numeros = []
opcao = ''
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    while opcao not in ['S', 'N']:
        opcao = str(input('Quer adcionar mais? [S/N] ')).upper().strip()[0]

    if opcao == 'S':
        opcao = ''
    else:
        break
print('-'*30)
print(f'lista {numeros}')
print('-'*30)
print(f'Ela tem {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Valores em ordem decrescente {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não está na lista')
