#CORES NO TERMINAL
from random import randint
import pygame
import time

pygame.init()
pygame.mixer.music.load('C:\\Users\\marco\\Music\\Bibi.mp3')
pygame.mixer.music.play()
pygame.mixer.music.play(loops=-1)

time.sleep(0.9)
print('\033[1;31m=-'*20)
time.sleep(1.3)
print('\033[0;36mJOGO DA ADIVINHAÇÃO!')
time.sleep(0.9)
print('\033[1;31m=-'*20)

time.sleep(1.6)
while True:
    time.sleep(1)
    n = int(input('\033[33mDigite um numero entre\033[m 0 e 10: '))
    a = randint(0, 10)

    time.sleep(1)
    if n == a:
        print('\033[1;32mParabéns vc acertou!\033[m O número era \033[36m{}'.format(a))
        print(' ')
        time.sleep(0.5)
        s = int(input('''\033[1;30;45mDESEJA JOGAR NOVAMENTE?\033[m
    \033[32m[1]SIM
    \033[31m[2]NÃO\033[m
    
    -> '''))
        if s == 1:
            time.sleep(0.6)
            print('\033[35mVamos de novo!! :P')

        elif s == 2:
            time.sleep(0.6)
            print('\033[35mAté mais! :)')
            break

    elif n>10:
        print('\033[35mEsse número é muito grade, tente outro menor ou igual a \033[4;34m10\033[m')
        print(' ')

    elif n == 000:
        print('\033[35mAté mais! :)')
        break

    else:
        print('\033[1;31mERROU!\033[m o numero era \033[36m{}'.format(a))

#while pygame.mixer.music.get_busy():
    #continue
