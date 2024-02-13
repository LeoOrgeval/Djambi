import pygame
from constantes import *
from Board import Board
from Pawn import Assassin, Reporter, Chief, Militant, Diplomat, Necromobile


# pygame setup
pygame.init()

# générer la fenêtre du jeu
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Djambi")

# Créer le plateau une seule fois
board = Board()

# Variable pour dire si la fenêtre est ouverte ou non
running = True

clock = pygame.time.Clock()

# dessiner un fond blanc entre le plateau (700x700) et un fond noir pour le reste de la fenêtre (1400x700)
screen.fill(color['WHITE'])
pygame.draw.rect(screen, color['BLACK'], (WIDTH, 0, WIDTH, HEIGHT))

# dessiner le plateau
board.display_board()

# mettre à jour l'affichage
pygame.display.flip()

# Création des instances de chaque type de pion avec différentes couleurs et positions

# Green Team
green_diplomat = Diplomat('green')
green_chief = Chief('green')
green_assassin = Assassin('green')
green_reporter = Reporter('green')
green_militant_0 = Militant('green', 0)
green_militant_1 = Militant('green', 1)
green_militant_2 = Militant('green', 2)
green_militant_3 = Militant('green', 3)
green_necromobile = Necromobile('green')
green_team = [green_diplomat, green_chief, green_assassin, green_reporter, green_militant_0, green_militant_1,
              green_militant_2, green_militant_3, green_necromobile]

# Yellow Team
yellow_diplomat = Diplomat('yellow')
yellow_chief = Chief('yellow')
yellow_assassin = Assassin('yellow')
yellow_reporter = Reporter('yellow')
yellow_militant_0 = Militant('yellow', 0)
yellow_militant_1 = Militant('yellow', 1)
yellow_militant_2 = Militant('yellow', 2)
yellow_militant_3 = Militant('yellow', 3)
yellow_necromobile = Necromobile('yellow')
yellow_team = [yellow_diplomat, yellow_chief, yellow_assassin, yellow_reporter, yellow_militant_0, yellow_militant_1,
               yellow_militant_2, yellow_militant_3, yellow_necromobile]

# Red Team
red_diplomat = Diplomat('red')
red_chief = Chief('red')
red_assassin = Assassin('red')
red_reporter = Reporter('red')
red_militant_0 = Militant('red', 0)
red_militant_1 = Militant('red', 1)
red_militant_2 = Militant('red', 2)
red_militant_3 = Militant('red', 3)
red_necromobile = Necromobile('red')
red_team = [red_diplomat, red_chief, red_assassin, red_reporter, red_militant_0, red_militant_1, red_militant_2,
            red_militant_3, red_necromobile]

# Blue Team
blue_diplomat = Diplomat('blue')
blue_chief = Chief('blue')
blue_assassin = Assassin('blue')
blue_reporter = Reporter('blue')
blue_militant_0 = Militant('blue', 0)
blue_militant_1 = Militant('blue', 1)
blue_militant_2 = Militant('blue', 2)
blue_militant_3 = Militant('blue', 3)
blue_necromobile = Necromobile('blue')
blue_team = [blue_diplomat, blue_chief, blue_assassin, blue_reporter, blue_militant_0, blue_militant_1, blue_militant_2,
             blue_militant_3, blue_necromobile]

# Show pawns for each team
for team in [green_team, yellow_team, red_team, blue_team]:
    for piece in team:
        pygame.draw.rect(screen, piece.color, (piece.position[0] * SQUARE_SIZE, piece.position[1] * SQUARE_SIZE,
                                               SQUARE_SIZE, SQUARE_SIZE))

        piece_image = pygame.image.load(piece.image)
        resized_piece_image = pygame.transform.scale(piece_image, piece.scale)

        screen.blit(resized_piece_image,
                    (piece.position[0] * SQUARE_SIZE + (SQUARE_SIZE - piece.scale[0]) // 2,
                     piece.position[1] * SQUARE_SIZE + (SQUARE_SIZE - piece.scale[1]) // 2))


# Dessiner les lignes de la grille
for i in range(1, ROWS):
    pygame.draw.line(screen, (0, 0, 0), (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE))
    pygame.draw.line(screen, (0, 0, 0), (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT))

# mettre à jour l'affichage
pygame.display.flip()

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
