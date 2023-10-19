# LOJA DE PRODUTOS
produtos = []
preco_barato = None
total = 0
mil_ou_mais = 0
opcao = ''
loja = ' SUPERMERCADO ATACADÃO '
print('—'*40)
print(f'{loja:—^40}')
print('—'*40)
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    total += preco

    if preco_barato is None or preco < preco_barato:
        preco_barato = preco
        produtos = [nome]
    elif preco == preco_barato:
        produtos.append(nome)

    if preco >= 1000:
        mil_ou_mais += 1

    while opcao not in ['S', 'N']:
        opcao = str(input('Quer cadastrar outra pessoa? [S/N] ')).upper().strip()[0]
    if opcao == 'S':
            print('====== NOVO PRODUTO ======')
            opcao = ''
    else:
        print(' ')
        break
print('------------- FIM DA COMPRA -------------')
print(f'-> VALOR DA COMPRA:            R${total:.2f}')
print(f'-> BARATO: "{", ".join(produtos)}"            R${preco_barato:.2f}')
print(f'-> MAIS DE R$ 1000.00          - {mil_ou_mais}')
print('-----------------------------------------')
