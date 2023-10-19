#masculino ou feminino
#se o usuario digitar algo diferente de "M", "m", "F", 'f' o programa repetirá a pergunta (n)

n = 1
sair = 0

while n != 0:
    n = str(input('\033[32mQual é o seu sexo? [M/F]\033[m '))
    if n in 'Mm':
        print('Você é homem!')
        n = sair
    elif n in 'Ff':
        print('Voce é mulher!')
        n = sair
    else:
        print('Você digitou um caracter incorreto. Escolha entre [M/F]')
