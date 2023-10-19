print('\033[31m='*23)
print('\033[31m=\033[33m EMPRÉSTIMO BANCÁRIO \033[31m=')
print('\033[31m='*23)
print('\033[m ')

c = float(input('Qual é o valor da casa? '))
s = float(input('De quanto é seu salário? '))
a = int(input('Em quantos anos quer pagar a casa? '))

paecelas = a * 12
valor = c / paecelas
salario = s * (30/100)

if valor > salario:
    print('Você não pode confirmar pois seu salário não é suficiente.')
elif valor <= salario:
    print('Você está ápto a fazer o empréstimo!')
    print('VALOR DAS PARCELAS POR MÊS: EM {} PARCELAS VOCÊ PAGARÁ R$ {:.2f} POR MÊS.'.format(paecelas, valor))  
