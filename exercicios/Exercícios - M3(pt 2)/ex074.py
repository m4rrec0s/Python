# DADOS
from random import randint
from time import sleep


jogadores = {}
cache = []
cont = 0

while True:
    if cont == 4:
        break
    sorteio = randint(1, 6)
    if sorteio not in jogadores.values():
        jogador = f'jogador{cont+1}'
        jogadores[jogador] = sorteio
        cont += 1

for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('-'*30)
print('Ranking dos jogadores:')
sleep(2)

jogadores_ordenados = dict(sorted(jogadores.items(), key=lambda x: x[1], reverse=True))

for i, (k, v) in enumerate(jogadores_ordenados.items(), start=1):
    print(f'{i}º lugar - {k} -> {v}')
    sleep(1)
print('-'*30)
