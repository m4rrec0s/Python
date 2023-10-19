num = 0
contador = 0
s = num
soma = 0
num = int(input('Digite um número (999 para parar): '))
while s != 999:
    if num != 999:
        soma += num
        contador += 1
        num = int(input('Digite um número (999 para parar): '))
    else:
        s = num
print('você digitou {} numeros e a soma entre eles foi de {}'.format(contador, soma))
