#PEDRA, PAPEL, TESOURA
import random
import time
from random import randint
from time import sleep

computador = random.randint(1, 3)

print('\033[35m='*6, 'JOKENPOL', '='*6, '\033[m')
opcoes_jogador = int(input('''Suas opções:
[ 1 ] pedra
[ 2 ] papel
[ 3 ] tesoura

-> '''))

time.sleep(0.3)
print('\033[33mJO\033[m')
time.sleep(0.6)
print('\033[34mKEN\033[m')
time.sleep(0.9)
print('\033[31mPO\033[m')

time.sleep(0.5)
print('='*10)
if computador == 1:
    print('O computador jogou \033[37mPEDRA!\033[m')
elif computador == 2:
    print('O computador jogou \033[7;37mPAPEL\033[m')
elif computador == 3:
    print('O computador jogou \033[34mTESOURA\033[m')

if opcoes_jogador == 1:
    print('Você jogou \033[37mPEDRA!\033[m')
elif opcoes_jogador == 2:
    print('Você jogou \033[7;37mPAPEL\033[m')
elif opcoes_jogador == 3:
    print('Você jogou \033[34mTESOURA\033[m')
else:
    print('\033[1;31mOpção inválida! tente novamente...\033[m')
print('='*10)

time.sleep(0.5)
if computador == opcoes_jogador:
    print('\033[33mEMPATE!\033[m')
elif computador == 1 and opcoes_jogador == 2:
    print('\033[32mVocê ganhou!\033[m')
elif computador == 2 and opcoes_jogador == 1:
    print('\033[31mComputador ganhou\033[m')
elif computador == 2 and opcoes_jogador == 3:
    print('\033[32mVocê ganhou!\033[m')
elif computador == 3 and opcoes_jogador == 2:
    print('\033[31mComputador ganhou\033[m')
elif computador == 1 and opcoes_jogador == 3:
    print('\033[31mComputador ganhou\033[m')
elif computador == 3 and opcoes_jogador == 1:
    print('\033[32mVocê ganhou!\033[m')
