import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuraciones de la ventana
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Juego de la Culebrita')

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Función para manejar el menú
def main_menu():
    menu = True
    selected = "play"
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    selected = "play" if selected == "quit" else "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "play":
                        # Aquí se iniciaría el juego
                        game()
                    else:
                        pygame.quit()
                        sys.exit()

        # Fondo de pantalla
        screen.fill(WHITE)

        # Dibujar las opciones del menú
        title = pygame.font.Font(None, 74).render('Menu Principal', True, (0, 0, 0))
        screen.blit(title, (160, 100))

        if selected == "play":
            play_text = pygame.font.Font(None, 50).render('Jugar', True, BLUE)
        else:
            play_text = pygame.font.Font(None, 50).render('Jugar', True, (0, 0, 0))
        if selected == "quit":
            quit_text = pygame.font.Font(None, 50).render('Salir', True, BLUE)
        else:
            quit_text = pygame.font.Font(None, 50).render('Salir', True, (0, 0, 0))

        screen.blit(play_text, (270, 200))
        screen.blit(quit_text, (270, 260))

        pygame.display.update()
        
def game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# Iniciar el menú principal
main_menu()

pygame.quit()
