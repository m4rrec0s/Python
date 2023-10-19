lista = []
cont = 0
opcao = ''
while True:
    n = int(input('Digite um valor único: '))
    if n not in lista:
        lista.append(n)
        print('Adicionado com sucesso!')
    else:
        print('O número já foi incerido. Tente novamente...')

    while opcao not in ['S', 'N']:
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'S':
            opcao = ''
    else:
        break
lista.sort()
print('-'*30)
print(f'Sua lista é formada pelos numeros {lista}.')
print ('-'*30)