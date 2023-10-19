def leiaInt(valor):
    '''
    -> Input que só recebe valores inteiros
    :param valor: Digite um valor inteiro
    :return: retorna o valor (n) se for inteiro
    '''
    while True:
        s = input(valor)
        try:
            n = int(s)
            return n
        except ValueError:
            print('\033[1;31mErro! Digite um número inteiro!\033[m')

# programa principal
n = leiaInt('Digite um número: ')
print(f'você digitou o número {n}')
