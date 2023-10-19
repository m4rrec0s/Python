n = 0
r = 'S'
soma = contador = media = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
    soma += n
    contador += 1
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / contador
print('Você digitou {} números e a média entre eles é {}'.format(contador, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
