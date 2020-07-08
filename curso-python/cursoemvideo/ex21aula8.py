#Abra e reproduza o audio de um arquivo mp3
'''import os
os.startfile(/home/roberta/Música/hinobrasileiro.mp3)'''
import pygame
pygame.init()
pygame.mixer.music.load('hinobrasileiro.mp3')
pygame.mixer.music.play()
pygame.event.wait()

