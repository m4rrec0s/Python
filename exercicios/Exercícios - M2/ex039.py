idades = 0
sexos = 0
idhomem = 0
nomehomaisvelho = ''
mulhermais20 = 0

for c in range(1, 5):
    print('==== {}ºpessoa ===='.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    if c == 1 and sexo in 'Mm':
        idhomem = idade
        nomehomaisvelho = nome
    if sexo in 'Mm' and idade > idhomem:
        idhomem = idade
        nomehomaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermais20 =+ 1

    idades += idade
    media = idades / 4

print(' ')
print('A média de idade do grupo é de \033[1;32m{}\033[m anos.'.format(media))
print('O homem mais velho tem \033[1;33m{}\033[m anos e se chama \033[1;33m{}\033[m.'.format(idhomem, nomehomaisvelho.capitalize()))
print('Existem \033[1;36m{}\033[m mulheres com menos de 20 anos'.format(mulhermais20))
