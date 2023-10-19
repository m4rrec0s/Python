from datetime import date

hoje = date.today()
ano_atual = hoje.year
dma = 0
dme = 0
for perguntas in range(1, 8):
    pessoas = int(input('Em que ano a {}º pessoa nasceu? '.format(perguntas)))
    calculo = ano_atual - pessoas
    if calculo >= 21:
        dma += 1
    else:
        dme += 1
print(' ')
print('''Das pessoas acima:
=============================================
{} SÃO PESSOAS DE \033[33mMAIOR\033[m IDADE ↑
{} SÃO PESSOAS DE \033[32mMENOR\033[m IDADE ↓
============================================='''.format(dma, dme))
