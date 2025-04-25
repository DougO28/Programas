import pygame
from config import *
from cubo import CuboRubik

pygame.init()
pantalla = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cubo de Rubik")
reloj = pygame.time.Clock()

cubo = CuboRubik()

def dibujar_cubo():
    tam = 30
    offset_x = 200
    offset_y = 50
    for i, cara in enumerate(['U', 'L', 'F', 'R', 'B', 'D']):
        x0 = offset_x + (i % 4) * tam * 3 if cara != 'U' and cara != 'D' else offset_x + tam * 3
        y0 = offset_y if cara == 'U' else offset_y + (1 if cara in ['L','F','R','B'] else 4) * tam
        for j in range(9):
            color = COLORES[cubo.caras[cara][j]]
            x = x0 + (j % 3) * tam
            y = y0 + (j // 3) * tam
            pygame.draw.rect(pantalla, color, (x, y, tam, tam))
            pygame.draw.rect(pantalla, (0, 0, 0), (x, y, tam, tam), 1)

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_u:
                cubo.mover_U()

    pantalla.fill((30, 30, 30))
    dibujar_cubo()
    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()

                                
