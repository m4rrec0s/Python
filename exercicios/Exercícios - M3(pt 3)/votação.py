# 65 anos opcional
import datetime

def idade(ano):
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano

def voto(ano):
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano
    
    if idade < 16:
        return 'NEGADO'
    elif idade >= 18 and idade < 65:
        return 'OBRIGATÓRIO'
    else:
        return 'OPCIONAL'

nasc = int(input('Informe seu ano de nascimento: '))
print(f'Com {idade(nasc)} anos: VOTO {voto(nasc)}')
