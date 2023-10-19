numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze' , 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove' , 'vinte')
while True:
    u = int(input('Digite um número entre 0 e 20: '))
    if u < 0 or u > 20:
        print('Tente novamente. ',end='')
    else:
        break
print(numeros[u])
