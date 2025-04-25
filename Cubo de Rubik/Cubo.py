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

#Movimientos

def mover_U(cubo):
    #Rota la cara U en sentido contrario
    cubo['U'] = rotar_horario(cubo['U'])

    #Mueve las filas superiores de las caras 

    temp = cubo['F'][:3]
    cubo['F'][:3] = cubo['R'][:3]
    cubo['R'][:3] = cubo['B'][:3]
    cubo['B'][:3] = cubo['L'][:3]
    cubo['L'][:3] = temp

#Funcion rotar cara
def rotar_horario(cara):
    return [cara[i] for i in [6,3,0,7,4,1,8,5,2]]



