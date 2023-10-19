#CALCULANDO O IMC
p = float(input('Qual é seu peso (kg)? '))
a = float(input('Qual é sua altura? (m) '))
calculo = (p / (a * a))

print('\033[1;34mIMC DE {:.2f}\033[m'.format(calculo))

if calculo < 18.5:
    print('Você está abaixo do peso')
elif calculo >= 18.5 and calculo <25:
    print('PESO IDEAL!')
elif calculo >= 25 and calculo <30:
    print('Você está com SOSBREPESO')
elif calculo >= 30 and calculo <40:
    print('Você está com OBESIDADE')
elif calculo > 40:
    print('Você está com OBESIDADE MÓRBIDA')
