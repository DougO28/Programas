import pygame
import sys

pygame.init()


width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cubo de Rubik")
#cubo de rubik


#variables globales
cubo = {
    'U': ['W']*9, #color blanco
    'U': ['Y']*9, #color amarillo
    'L': ['O']*9, #Color anaranjado
    'R': ['R']*9, #color rojo
    'F': ['G']*9, #color verde
    'B': ['B']*9  #color azul
}

