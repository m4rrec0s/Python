from datetime import date
ano_atual = date.today().year
pessoa = {}
pessoa['Nome'] = str(input('Nome: ')).capitalize().split()
idad = int(input('Ano de Nascimento: '))
pessoa['idade'] = ano_atual - idad
while True:
    carteira = int(input('Carteira de Trabalho [0 não tem]: '))
    if carteira == 0:
        break
    else:
        pessoa['CTPS'] = carteira
        pessoa['Contratação'] = int(input('Ano de contratação: '))
        pessoa['Salário'] = int(input('Salário: \033[32mR$\033[m'))
        pessoa['Aposentadoria'] = pessoa['idade'] + 35
        break

# print simples

print('-'*30)
for k, v in pessoa.items():
    print(f' ⇒ {k} é igual a {v}')
print('-'*30)

# print longo

print(f'O(a) Sr.(a) {pessoa["Nome"][0]} tem {pessoa["idade"]} anos de idade.')
if carteira != 0:
    print(f'''O número da CTPS de {pessoa['Nome'][0]} é "{pessoa['CTPS']}"
O ano de contratação foi {pessoa['Contratação']}.
O salário era de {pessoa['Salário']}
A aposentadoria de {pessoa['Nome'][0]} está prevista para os {pessoa['Aposentadoria']} anos de idade''')
print('-'*30)
