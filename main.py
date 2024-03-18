import pygame
from constantes import *
from board import Board

# pygame setup
pygame.init()

# générer la fenêtre du jeu
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Djambi")

# Créer le plateau une seule fois
board = Board(screen)

# Afficher les pièces
board.display_pieces()

board.display()

# Variable pour dire si la fenêtre est ouverte ou non
running = True

clock = pygame.time.Clock()



# Boucle tant que running est vrai
while running:
    # si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # si l'événement est 'la fermeture de la fenêtre'
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # si l'événement est un clic de souris, changer la position de la pièce sélectionnée par le joueur
        if event.type == pygame.MOUSEBUTTONDOWN:
            # obtenir la position de la souris
            pos = pygame.mouse.get_pos()
            # convertir la position de la souris en coordonnées de la grille
            row = pos[1] // SQUARE_SIZE
            col = pos[0] // SQUARE_SIZE
            print(row, col)

        # mettre à jour l'affichage
        pygame.display.flip()

    clock.tick(FPS)
