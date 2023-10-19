from time import sleep

def contagem(a, b, c):
    print('—'*30)
    if c == 0:
        c = 1

    if b > a:
        print(f'Contagem de {a} até {b} de {c} em {c}:')
        for d in range(a, b+1, c):
            print(d, end=' ')
            sleep(0.5)
        print('FIM!')

    elif b < a:
        ps = abs(c)
        print(f'Contagem de {a} até {b} de {ps} em {ps}')
        for d in range(a, b-1, ps * -1):
            print(d, end=' ')
            sleep(0.5)
        print('FIM!')


contagem(1, 10, 1)
contagem(10, 1, -1)
print('—'*30)
print('Chegou a hora de você mesmo criar sua contagem:')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(inicio, fim, passo)
print('—'*30)
