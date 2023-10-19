# CAIXA ELETRONICO
cinquenta_reais = vinte_reais = dez_reais = um_real = 0
print('-'*40)
print('{:^40}'.format('BANCO MARRECOS'))
print('-'*40)
valor = int(input('Quanto você quer sacar? '))
while True:
    if valor >= 50:
        valor -= 50
        cinquenta_reais += 1
    elif valor < 50 and valor >= 20:
        valor -= 20
        vinte_reais += 1
    elif valor < 20 and valor >= 10:
        valor -= 10
        dez_reais += 1
    elif valor <10 and valor > 0:
        valor -= 1
        um_real += 1
    elif valor == 0:
        break
print('-'*40)
print('{:^40}'.format('TOTAL DE CÉDULAS'))
print('-'*40)
if cinquenta_reais > 0:
    print(f'{cinquenta_reais} NOTAS DE R$ 50.00')
if vinte_reais > 0:
    print(f'{vinte_reais} NOTAS DE R$ 20.00')
if dez_reais > 0:
    print(f'{dez_reais} NOTAS DE R$ 10.00')
if um_real > 0:
    print(f'{um_real} NOTAS DE R$ 1.00')
print('-'*40)
