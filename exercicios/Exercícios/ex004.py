#DE REAIS PARA DÓLARES
n = float(input('Quantos Reais você tem na carteira? '))
d = (n / 3.27)
print('COTAÇÃO DO DÓLAR ATUAL: R$3.27')
print('Você pode comprar US${:.2f} com R${}.'.format(d, n))
print('='*15)
#PINTANDO UMA PAREDE
n1 = int(input('Quantos metros de largura tem sua parede? '))
n2 = int(input('Quantos metros de altura tem sua parede? '))
r = (n1 * n2)
r1 = (r / 2)
print('='*15)
print('''
Será necessário usar {} laras de tinta para pintar esta parede.
'''.format(r1))
print('='*15)
