n1 = float(input('CATETO 1: '))
n2 = float(input('CATETO 2: '))
n3 = float(input('CATETO 3: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Os segmentos PODEM formar um triâgulo!')
    if n1 == n2 and n2 == n3 and n1 == n3:
        print('TRIANGULO EQUILÁTERO - TODOS OS LADOS IGUAIS')
    elif n1 == n2 and n3 != n1 and n3 != n2 or n1 != n2 and n2 == n3 and n3 != n1 or n1 == n3 and n2 !=n3:
        print('TRIAGULO ISÓRCELES - 2 LADOS IGUAIS')
    elif n1 != n2 and n3 != n1 and n3 != n2:
        print('TRIANGULO ESCALENO - TODOS OS LADOS DIFERENTES')

else:
    print('Os segmentos NÃO PODEM formar um triângulo')
