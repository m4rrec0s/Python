print('=-'*20)
print(' '*10, 'Gerador de PA')
print('=-'*20)
n1 = int(input('Digite um número: '))
razao = int(input('Razão: '))
termo = n1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Adicionar mais quantos numeros? '))
print('=-'*20)
print('{} termos da PA de 1º termo - {} e razão {}.'.format(cont, n1, razao))
