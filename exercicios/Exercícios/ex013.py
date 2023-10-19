from random import randint
import pygame

pygame.init()
pygame.mixer.music.load('C:\\Users\\marco\\Music\\Bibi.mp3')
pygame.mixer.music.play()

while True:
    n = int(input('Digite um numero entre 0 e 5: '))
    a = randint(0, 5)

    if n == a:
        print('Parabens vc acertou! O número era {}'.format(a))
        break
    else:
        print('ERROU! o numero era {}'.format(a))

#while pygame.mixer.music.get_busy():
    #continue