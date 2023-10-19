numeros = list()
for cont in range(0,5):
    n = int(input(f'Digite o {cont + 1}º valor: '))

    for chave, valor in enumerate(numeros):
        if n < valor:
            numeros.insert(chave, n)
            print(f'Adcionado na posição: {chave+1}º')
            break
    else:
        print('Adcionado no fim da lista...')
        numeros.append(n)
print('-'*30)
print(f'Sua lista é composta pelos números: {numeros}')
