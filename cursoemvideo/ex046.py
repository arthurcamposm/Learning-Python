from time import sleep
import pygame
print('OS FOGOS VÃO ESTOURAR EM...')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
pygame.init()
pygame.mixer.music.load('fogos.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait(13)
print('FIM')