from random import randint
from time import sleep
jogo = []
cache = []
print(f'{"> SORTEADOR <":-^40}')
opcao = int(input('Quer que eu sorteie quantos jogos? '))
for c in range(opcao):
    while len(cache) < 6:
        sorteio = randint (1, 60)
        if sorteio not in cache:
            cache.append(sorteio)
    jogo.append(cache[:])
    cache.clear()
print ('-' * 40)
print(f'{f" SORTEANDO {opcao} JOGOS ":^40}')
print('-'*40)
sleep(0.5)
for q, n in enumerate(jogo):
    print(f'Jogo {q+1}:  ',end='')
    sleep(0.3)
    print(sorted(n), end='')
    print()
    sleep(0.6)
print(f'{"> BOA SORTE <":-^40}')
