def fatorial(num=1, show=False):
    '''
    -> Calcula o fatorial de um número
    :param num: O núnero a ser analizado
    :param show: (opcional) mostra a conta
    :return: retorna o valor do fatorial do número (num)
    '''

    f = 1
    if show == False:
        for c in range(num, 0, -1):
            f *= c
        print(f)
    else:
        for c in range (num, 0, -1):
            if c == 1:
                print (f'{c} = ', end='')
            else:
                print (f'{c} x ', end='')
            f *= c
        print (f)
print()
print('-'*40)
# programa principal
fatorial(5, True)
print('-'*40)
help(fatorial)
