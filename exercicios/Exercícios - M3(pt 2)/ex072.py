alunos = []
cache = []
média = 0
print('CADASTRO DE ALUNOS ⁂')
while True:
    cache.append(str(input('Nome: ')))
    cache.append(float(input('Nota 1: ')))
    cache.append(float(input('Nota 2: ')))
    alunos.append(cache[:])
    cache.clear()
    opcao = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
    if opcao == 'N':
        break
print('--'*30)
print(f'No. NOME {"MÉDIA":>31}')
print('--'*30)
for d, n in enumerate(alunos):
    média = (n[1] + n[2]) / 2
    print(f'{d}   {n[0]:<30} {média:<4.1f}', end='')
    print()
print('--'*30)
while True:
    op2 = int(input('Mostrar notas de qual aluno? [No.] [999 to exite]: '))
    if op2 == 999:
        break
    print(f'Notas de {alunos[op2][0]} : {alunos[op2][1]} e {alunos[op2][2]}')
    print('--' * 30)
print('-' * 60)
print(f'{"....PROGRAMA FINALIZADO....":-^60}')
print(f'{"ATÉ MAIS":^60}')
