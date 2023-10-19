n = int(input('Digite um número: '))

if n % 2 == 0:
    print(f'{n} é um número PAR')
else:
    print(f'{n} é um número IMPAR ')

print('=='*20)

v = int(input('Qual a distância da sua viagem (em Km)'))

if v > 200:
    p = v - 200
    r = (200 * 0.50) + (p * 0.45)
    print('Sua passagem custará R${}'.format(r))
else:
    print('Sua passagem custará R${}'.format(v * 0.50))

