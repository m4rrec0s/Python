#IDADE DOS ATLETAS
from datetime import date

data_nascimento = int(input('Qual sua Data de Nascimento? '))
idade = date.today().year - data_nascimento
print(idade,'anos')

if idade <= 9:
    print('Você está na categoria MIRIM.')
elif idade > 9 and idade <= 14:
    print('Você está na categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Você está na categoria JUNIOR')
elif idade > 19 and idade <= 25:
    print('Você está na categoria SÊNIOR')
elif idade >= 25:
    print('Você está na categoria MASTER')
