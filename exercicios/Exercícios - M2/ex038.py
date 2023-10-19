#maior e menor peso
maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Quanto a {}ª pessoa pesa? '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(' ')
print('='*25)
print('O maior peso é de {} Kg'.format(maior))
print('O menor peso é de {} Kg'.format(menor))
print('='*25)
