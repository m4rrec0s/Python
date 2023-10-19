from time import sleep
lista = []
def maior_valor(*num):
    print('Analizando valores passados...')
    sleep(1)
    for n in lista:
        print(n, end=', ')
        sleep(0.5)
    print(f'Foram informados {len(lista)} valores ao todo.')
    if len(lista) == 0:
        print('Não há valores na lista')
    else:
        print(f'O maior valor entre eles é {max(lista)}')
    print('-'*40)


print('-'*40)

lista = [4, 6, 1, 9, 17]
maior_valor(lista)
lista.clear()

lista = [6, 4, 10]
maior_valor(lista)
lista.clear()

lista = [9, 3]
maior_valor(lista)
lista.clear()

lista = [4]
maior_valor(lista)
lista.clear()

lista = []
maior_valor()

print('<< FIM >>')
