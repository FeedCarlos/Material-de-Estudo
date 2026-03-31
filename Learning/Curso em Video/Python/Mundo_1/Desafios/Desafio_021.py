# Faça um programa em Python que abra e reproduza um áudio de um arquivo MP3.

import pygame
import time

pygame.mixer.init()
caminho_mp3 = "C:/Users/rafae/Documents/Curso em Video/Python/Extra/teste.mp3"
pygame.mixer.music.load(caminho_mp3)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)
pygame.quit()