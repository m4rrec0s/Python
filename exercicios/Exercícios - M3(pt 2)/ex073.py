# USANDO DISCIONÁRIOS
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['média'] = float(input(f'Média de {pessoa["nome"]}: '))
if pessoa['média'] >= 7.0:
    pessoa['situação'] = 'Aprovado'
else:
    pessoa['situação'] = 'Reprovado'
print('-'*30)
for k, v in pessoa.items():
    print(f'{k} é {v}')
print('-'*30)
