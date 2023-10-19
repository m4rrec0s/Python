# IDADE E SEXO
opcao = ''
sexo = ''
cont_I = 0
cont_M = 0
cont_F = 0

print('===== CADASTRO DE PESSOAS =====')
while True:
    idade = int(input('IDADE: '))
    if idade >18:
        cont_I += 1
    while sexo not in ['M', 'F']:
        sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
        if sexo == 'M':
            cont_M += 1
        elif idade >20 and sexo == 'F':
            cont_F += 1
    while opcao not in ['S', 'N']:
        opcao = str(input('Quer cadastrar outra pessoa? [S/N] ')).upper().strip()[0]
    if opcao == 'S':
            print('==== NOVO CADASTRO ====')
            sexo = ''
            opcao = ''
    else:
        break
print('======================')
print('===== RESULTADOS =====')
print(f'PESSOAS COM MAIS DE 18 ANOS: {cont_I}')
print(f'HOMENS CADASTRADOS: {cont_M}')
print(f'MULHERES COM + DE 20 ANOS: {cont_F}')
