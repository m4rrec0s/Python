pessoas = []

while True:
    people = {}
    people['Nome'] = str(input('Nome: ')).capitalize()

    people['sexo'] = ''
    while people['sexo'] not in 'M' or 'F':
        people['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if people['sexo'] not in 'MF':
            print('Digite apenas "M" ou "F"')
        else:
            break

    people['idade']= int(input('Idade: '))
    pessoas.append(people.copy())
    del people

    opcao = ''
    while opcao not in 'S' or 'N':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if opcao not in 'SN':
            print('Digite apenas "S" ou "N"')
        else:
            break
    if opcao == 'N':
        break

print('-'*30)
print(f'{"CONCLUÍDO!":^30}')
print('-'*30)
print(f'{len(pessoas)} pessoas cadastradas.')

for v in pessoas:
    print(v)
print('-'*30)

soma_idades = sum(people['idade'] for people in pessoas)
media = soma_idades / len(pessoas)
print(f'A média de idade é {media:.2f}')

mulheres = []
for person in pessoas:
    if 'F' == person['sexo']:
        mulheres.append(person['Nome'])
print(f'No programa, as mulheres cadastradas foram: {", ".join(mulheres)}')

acima_media = []
for person in pessoas:
    if person['idade'] > media:
        acima_media.append(person['Nome'])
print(f'As pessoas com a idade acima da média são: {", ".join(acima_media)}')
print('-'*30)
