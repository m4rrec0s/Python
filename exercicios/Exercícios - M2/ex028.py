print('='*6, 'LOJAS MARRECOS', '='*6)

vp = float(input('Qual o valor da compra? R$'))
fp = int(input('''Qual a forma de pagamento?

[ 1 ] à vista dinheiro/cheque: (10% de desconto) 
[ 2 ] à vista no cartão: (5% de desconto)
[ 3 ] em até 2x no cartão: (preço normal) 
[ 4 ] 3x ou mais no cartão: (20% de juros)

: '''))

if fp == 1:
    print('PAGAMENTO À VISTA/CHEQUE: ')
    calculo1 = vp - (vp * (10/100))
    print('Total a  pagar: {:.2f}'.format(calculo1))
elif fp == 2:
    print('PAGAMENTO À VISTA NO CARTÃO: ')
    calculo1 = vp - (vp * (5 / 100))
    print('Total a  pagar: {:.2f}'.format(calculo1))
elif fp == 3:
    print('PAGAMENTO EM ATÉ 2x NO CARTÃO: ')
    calculo1 = vp/2
    print('Total a  pagar: 2x de R${:.2f}.'.format(calculo1))
elif fp == 4:
    print('PAGAMENTO EM 3x OU MAIS NO CARTÃO: ')
    opcao = int(input('-> Em quantas parcelas? '))
    calculo1 = vp + (vp * (20 / 100))
    parcelas = calculo1 / opcao
    if opcao >2:
        print('Você pagará {}x de R${:.2f}'.format(opcao, parcelas))
    elif opcao <=2:
        print('Quantidades de parcelas muito baixa. Tente de novo!')
else:
    print('valor inválido')
