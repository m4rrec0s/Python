geral = list()
maior = menor = 0

while True:
    nome = str (input ('Nome: '))
    peso = float (input ('Peso: '))

    pessoas = (nome, peso)
    geral.append(list(pessoas))

    opcao = input ('Quer continuar? [S/N]: ').strip().upper()[0]

    if opcao == 'N':
        break

print('--'*30)
print (f'{len (geral)} PESSOAS FORAM CADASTRADAS.')

# Inicialize o maior e o menor com o peso da primeira pessoa
maior = menor = geral[0][1]

for nome, peso in geral:
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso foi de {maior} kg - ', end='')
print(', '.join([p[0] for p in geral if p[1] == maior]))

print(f'O menor peso foi de {menor} kg - ', end='')
print(', '.join([p[0] for p in geral if p[1] == menor]))
