# Enquanto verdadeiro e o comando de parada (break)
while True:
	N = int(input('Digite um número: '))
	if N == 999:
		break
print('Acabou')

# f(str)

idade = 87
nome = 'João'
salário = 1500.8

print(f'O {nome} tem {idade} e recebe R${salário:.2f}.')
