#TABUADA
while True:
    print('-' * 40)
    n = int(input('Digite um número para ver a tabuada: '))
    if n <0:
        print('-' * 40)
        print('--- PROGRAMA FINALIZADO. ATÉ MAIS! ---')
        print('-' * 40)
        break
    for c in range(1, 11):
        r = n * c
        print(f'{n} x {c} = {r}')
