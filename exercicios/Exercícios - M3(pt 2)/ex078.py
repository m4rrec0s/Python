todos = []
cont = 0
while True:
    jogador = {}

    jogador['Nome'] = str(input('Nome do jogador: ')).capitalize()
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols = []
    for p in range(jogador['Partidas']):
        golsp = int(input(f'Quantos gols na partida {p+1}? '))
        gols.append(golsp)
    jogador['Gols'] = gols.copy()
    jogador['Total'] = sum(gols)
    todos.append(jogador.copy())
    del jogador

    opcao = ''
    while opcao not in 'S' or 'N':
        opcao = str (input ('Quer continuar? [S/N] ')).upper ().strip ()[0]
        if opcao not in 'SN':
            print ('Digite apenas "S" ou "N"')
        else:
            break
    if opcao == 'N':
        break

print('-'*46)
# print completo
print(f' cod. {"nome":<15}{"gols":<20}{"total":<2}')
print('-'*46)

for i, v in enumerate(todos):
    print(f'{i+1:>3}   {v["Nome"]:<15}{str(v["Gols"]):<20}{v["Total"]:<2}')
    cont += 1
print('-'*46)

while True:
    op2 = int(input('Mostrar dados de qual jogador? [999 para sair] '))
    op2 -= 1

    if op2 == 998:
        break

    elif op2 <= cont:
        print(f'LEVANTAMENTO DO JOGADOR - {todos[op2]["Nome"].upper()}:')
        for i, c in enumerate(todos[op2]["Gols"]):
            print(f'      -- No jogo {i} fez {c} gols.')
    if op2 > cont and op2 <998:
        print ('Código do jogador não cadastrado...')
    print ('-' * 46)

print ('-' * 46)
print('ENCERRADO')
