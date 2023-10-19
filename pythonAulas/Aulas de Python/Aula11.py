galera = [['João', 33], ['Marcos', 19], ['Magna', 40], ['Sérgio', 46]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

# ex 2
print('-'*30)
galera2 = list()
dado = list()
maior = menor = 0
for p in range(4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])# é importante fazer a cópia para não haver erro
    dado.clear()

for d in galera2:
    if d[1] >= 21:
        print(f'{d[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{d[0]} é menor de idade.')
        menor += 1
print('-'*30)
print(f'{maior} pessoas de maior.')
print(f'{menor} pessoas de menor')
