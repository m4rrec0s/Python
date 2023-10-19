print('=='*20)
print('ANALIZADOR DE TRIÂNGULOS')
print('=='*20)

a = float(input('-> Vértice 1: '))
b = float(input('-> Vertice 2: '))
c = float(input('-> V´tice 3: '))

if a < b + c and b < a + c and c < b + a:
    print('Os segmentos PODEM formar um triêgulo!')
else:
    print('Os segmentos NÃO PODEM formar um triângulo')

