#i have a archive .mp3,  you need create one too, for make this song play. Use my archive like a example
import pygame
pygame.init()
pygame.mixer.music.load('dua lipa.mp3')
pygame.mixer.music.play()
pygame.event.wait()
#pygame.mixer.music.stop()
