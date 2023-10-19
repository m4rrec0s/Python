for num in range(2, 51, 2):
    print(num, end=' ')
print('Fim!')

s=0
d = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        d += 1
print('a soma dos {} números multiplos de 3 e impares é {}'.format(d, s))
