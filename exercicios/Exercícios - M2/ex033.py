s = 0
co = 0
for c in range(1, 7):
    v = int(input('Digite o {}º valor: '.format(c)))

    if v %2 == 0:
        s += v
        co += 1

print('A soma dos {} valores PARES é: {}'.format(co, s))
