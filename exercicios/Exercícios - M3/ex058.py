numeros = (int(input('Digite um numero: ')),int(input('Digite um numero: '))
           ,int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'{numeros}')
print('—'*20)
print(f'o numero 9 aparece {numeros.count(9)} vezes')
print('—'*20)
if 3 in numeros:
    print(f'o prmeiro 3 apareceu na posição {numeros.index(3)+1}')
else:
    print('o numero 3 não apareceu em nunhum momento')
print('—'*20)
print('Os números pares são:', end='')
for n in numeros:
    if n %2 == 0:
        print(f' {n}', end='')
print('—'*20)
