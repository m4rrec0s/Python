jogador = {}

jogador['Nome'] = str(input('Nome do jogador: ')).capitalize()
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
gols = []
for p in range(jogador['Partidas']):
    golsp = int(input(f'Quantos gols na partida {p}? '))
    gols.append(golsp)
jogador['Gols'] = gols.copy()
jogador['Total'] = sum(gols)
# print básico
print('-'*30)
print(jogador)
print('-'*30)
# print com for
for k, v in jogador.items():
    print(f'- o campo {k} tem o valor {v}')
print('-'*30)
# print completo
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas:')
for i, v in enumerate(jogador['Gols']):
    print(f'    ⇒ Na partida {i}, fez {v}')
print(f'Foi um total de {jogador["Total"]} gols')
print('-'*30)
