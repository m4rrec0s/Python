#exercício 38 - curso
#MAIOR, MENOR OU IGUAL

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

maior = n1
if n2>n1:
    maior = n2
    print('O maior valor é {}.'.format(maior))
menor = n2
if n1<n2:
    menor = n1
    print('O menor valor é {}.'.format(menor))
elif n1 == n2:
    print('Os dois tem o mesmo valor.')
