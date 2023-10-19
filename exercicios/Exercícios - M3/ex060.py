lista = ('alegria', 'amor', 'beleza', 'carinho', 'chuva', 'coragem',
         'esperança', 'felicidade', 'flores', 'liberdade', 'luz', 'maravilha',
         'natureza', 'paz', 'sabedoria', 'saudade', 'serenidade',
         'sorriso', 'tranquilidade', 'vida')
vogais = ('a', 'e', 'i', 'o', 'u')
n = 0
print ('VOGAIS DE CADA PALAVRA')
for c in lista:
    print (f'\nNa palavra {c.upper()} temos: ', end='')
    for letra in c:
        if letra in vogais:
            print(letra, end=' ')
