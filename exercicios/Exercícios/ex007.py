import random

a1 = input('-> nome do 1 aluno: ')
a2 = input('-> nome do 2 aluno: ')
a3 = input('-> nome do 3 aluno: ')
a4 = input('-> nome do 4 aluno: ')

opcoes = [a1, a2, a3, a4]
random.shuffle(opcoes)

print("-- O ALUNO SORTEADO FOI --")
print(opcoes[0])
print('=-'*20)

print("A ordem aleatória dos nomes é:")
for i, nome in enumerate(opcoes):
    print(f"{i+1}º: {nome}")
print('=-'*20)
