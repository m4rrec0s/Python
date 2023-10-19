n1 = int(input('-> Digite um número: '))
n2 = int(input('-> Digite outro número: '))
n3 = int(input('-> Digite outro número: '))

menor = n1

if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1

if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
