#CAlCULANDO VARIANTES
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))

s = (n1 + n2)
su = (n1 - n2)
m = (n1 * n2)
d = (n1 / n2)
di = (n1 // n2)
p = (n1 ** n2)

print('''
RESULTADOS

A soma: {}
A subtração: {}
A multiplicação: {}
A divisão: {}
A divisão inteira: {}
A Potencia: {}'''.format(s, su, m, d, di, p))
