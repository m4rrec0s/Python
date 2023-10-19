#Desafio 39 - curso de python
#ALISTAMENTO
import datetime
from datetime import date

print('\033[32m==== ALIST\033[33mAMENTO ====\033[m')

data_atual = date.today()
data_atual_formatada = data_atual.strftime("%d-%m-%Y")
print('\033[4;34mHOJE - {}\033[m'.format(data_atual_formatada))

dia = int(input('Em qual dia você nasceu? '))
mes = int(input('Em qual mês você nasceu? '))
ano = int(input('Em que ano você nasceu? '))

data_nascimento = datetime.date(ano, mes, dia)
calculo_idade = (data_atual - data_nascimento)
result = int(calculo_idade.days / 365.25)
print('\033[1;36m%d anos\033[m' %(result))

if result == 18:
    print('Você deve se alistar neste ano!')

elif result < 18:
    anos_q_faltam = (18 - result)
    print('faltam {:.0f} anos para você se apresentar. Alistamento previsto para {}'.format(anos_q_faltam, date.today().year + anos_q_faltam))

elif calculo_idade > 0 and calculo_idade < 1:
    print('Falta menos de 1 ano para você se alistar')

elif result > 18:
    anos_q_passaram = (result - 18)
    print('''Passaram-se %d anos do seu alistamento. 
Se não se apresentou ainda, você está em \033[1;31mdébito\033[m com a 
\033[1;33Junta Militar Brasileira\033[m desde {}.'''.format(date.today().year - anos_q_passaram) %(anos_q_passaram))
