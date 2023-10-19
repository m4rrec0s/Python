n = int(input('Qual a velocidade do carro? '))

if n > 80:
    print('''Você ultrapassou a velocidade tolerante.
sua multa é de: R${}'''.format(int(n-80)*7))

else:
    print('')
