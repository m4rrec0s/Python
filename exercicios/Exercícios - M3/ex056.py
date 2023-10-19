times = ('Botafogo', 'Palmeiras', 'Red Bull Bragantino', 'Fluminense', 'Grêmio', 'Flamengo',
         'Fortaleza', 'Athletico-PR', 'Atlético-MG', 'Cuiabá', 'Cruzeiro', 'Internacional',
         'São Paulo', 'Corinthians', 'Goiás', 'Bahia', 'Santos', 'Vasco', 'América-MG',
         'Coritiba')

print ('-' * 30)
print ('Os 5 primeiros colocados são: ', times[0:5])
print ('-' * 30)
print ('Os 4 ultimos colocados são: ', times[-4:])
print ('-' * 30)
print ('Times em ordem alfábética:', sorted (times))
print ('-' * 30)
print (f'O time do Famengo está na posição: {times.index ("Flamengo") + 1}º')
print ('-' * 30)
