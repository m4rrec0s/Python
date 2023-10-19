import pygame

pygame.init()
pygame.mixer.music.load('C:\\Users\\marco\\Music\\Bibi.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue
