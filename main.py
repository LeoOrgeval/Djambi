import pygame
from constantes import *
from board import Board

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
screen.fill(WHITE)
pygame.draw.rect(screen, BLACK, (WIDTH, 0, WIDTH, HEIGHT))

# dessiner le plateau
board.display_board()

# mettre à jour l'affichage
pygame.display.flip()

green_pieces = ['Chief', 'Assassin', 'Militant',
                'Diplomate', 'Reporter', 'Militant',
                'Militant', 'Militant', 'Necromobile']
green_locations = [(0, 0), (1, 0), (2, 0),
                   (0, 1), (1, 1), (2, 1),
                   (0, 2), (1, 2), (2, 2)]

yellow_pieces = ['Militant', 'Assassin', 'Chief',
                 'Militant', 'Reporter', 'Diplomate',
                 'Necromobile', 'Militant', 'Militant']
yellow_locations = [(6, 0), (7, 0), (8, 0),
                    (6, 1), (7, 1), (8, 1),
                    (6, 2), (7, 2), (8, 2)]

red_pieces = ['Militant', 'Militant', 'Necromobile',
              'Diplomate', 'Reporter', 'Militant',
              'Chief', 'Assassin', 'Militant']
red_locations = [(0, 6), (1, 6), (2, 6),
                 (0, 7), (1, 7), (2, 7),
                 (0, 8), (1, 8), (2, 8)]

blue_pieces = ['Necromobile', 'Militant', 'Militant',
               'Militant', 'Reporter', 'Diplomate',
               'Militant', 'Assassin', 'Chief']
blue_locations = [(6, 6), (7, 6), (8, 6),
                  (6, 7), (7, 7), (8, 7),
                  (6, 8), (7, 8), (8, 8)]

chief = pygame.image.load('assets/chef-150x150.png')
chief = pygame.transform.scale(chief, (57, 57))
assassin = pygame.image.load('assets/assassin-150x150.png')
assassin = pygame.transform.scale(assassin, (57, 57))
diplomate = pygame.image.load('assets/diplomate-150x150.png')
diplomate = pygame.transform.scale(diplomate, (57, 57))
reporter = pygame.image.load('assets/reporter-150x150.png')
reporter = pygame.transform.scale(reporter, (57, 57))
necromobile = pygame.image.load('assets/necromobile-150x150.png')
necromobile = pygame.transform.scale(necromobile, (57, 57))
militant = pygame.image.load('assets/militant-150x150.png')
militant = pygame.transform.scale(militant, (57, 57))
maze = pygame.image.load('assets/chef-150x150.png')
maze = pygame.transform.scale(maze, (57, 57))

pieces_image = [chief, assassin, reporter, necromobile, diplomate, militant]
pieces_list = ['Chief', 'Assassin', 'Reporter', 'Necromobile', 'Diplomate', 'Militant']

# Afficher les pièces
for i in range(len(green_pieces)):
    for j in range(len(pieces_list)):
        if green_pieces[i] == pieces_list[j]:
            pygame.draw.rect(screen, GREEN, (green_locations[i][0] * SQUARE_SIZE, green_locations[i][1] *
                                             SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)),
            screen.blit(pieces_image[j],
                        (green_locations[i][0] * SQUARE_SIZE + 10, green_locations[i][1] * SQUARE_SIZE + 10)),

for i in range(len(yellow_pieces)):
    for j in range(len(pieces_list)):
        if yellow_pieces[i] == pieces_list[j]:
            pygame.draw.rect(screen, YELLOW, (yellow_locations[i][0] * SQUARE_SIZE, yellow_locations[i][1] *
                                              SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)),
            screen.blit(pieces_image[j],
                        (yellow_locations[i][0] * SQUARE_SIZE + 10, yellow_locations[i][1] * SQUARE_SIZE + 10))

for i in range(len(red_pieces)):
    for j in range(len(pieces_list)):
        if red_pieces[i] == pieces_list[j]:
            pygame.draw.rect(screen, RED, (red_locations[i][0] * SQUARE_SIZE, red_locations[i][1] *
                                           SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)),
            screen.blit(pieces_image[j],
                        (red_locations[i][0] * SQUARE_SIZE + 10, red_locations[i][1] * SQUARE_SIZE + 10))

for i in range(len(blue_pieces)):
    for j in range(len(pieces_list)):
        if blue_pieces[i] == pieces_list[j]:
            pygame.draw.rect(screen, BLUE, (blue_locations[i][0] * SQUARE_SIZE, blue_locations[i][1] *
                                            SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)),
            screen.blit(pieces_image[j],
                        (blue_locations[i][0] * SQUARE_SIZE + 10, blue_locations[i][1] * SQUARE_SIZE + 10))

# Maze piece in the middle board
pygame.draw.rect(screen, GREY, (4 * SQUARE_SIZE, 4 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
screen.blit(maze, (4 * SQUARE_SIZE + 10, 4 * SQUARE_SIZE + 10))

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
    clock.tick(FPS)
