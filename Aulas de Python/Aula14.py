def somar(a=0, b=0, c=0):
    '''
    -> Função para somar valores
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    :return: não retorna
    '''
    s = a + b + c
    print(f'A soma dos valores foi de {s}')

def verMai(a=0, b=0, c=0):
    m = max(a, b, c)
    return m

somar (2, 5)
somar(5, 9)

print(f'O maior valor foi {verMai(4, 1, 9)}')

print('-'*40)

def par(num=1):
    if num %2 == 0:
        return True
    else:
        return False

n1 = int(input('Digite um número: '))
if par(n1) == True:
    print('É par!')
else:
    print('É impar')
