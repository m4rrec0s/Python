#SUCESSOR E ANTECESSOR
n = int(input('Digite um número: '))
s = (n + 1)
a = (n - 1)
print('O sucessor deste número é: {} e o antecessor é: {}'.format(s, a))

q = input('''Quer continuar no exercício
[S] sim
[N] não
:''')

if q == "S" or "N" or "sim" or "não" or "n" or "s":
    #DOBRO, TRIPLO E A RAIZ QUADRADA
    print('OK')
    n2 = int(input('Digite um número: '))
    d = (n2 * 2)
    t = (n2 * 3)
    r = (n2 ** (1/2))
    print('''
    
Seu número: {}
O Dobro do número: {}
O Triplo do número: {}
A Raiz Quadrada do número: {}'''.format(n2, d, t, r))

else:
    exit()
