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
# green_locations = [(0, 0), (1, 0), (2, 0),
#                    (0, 1), (1, 1), (2, 1),
#                    (0, 2), (1, 2), (2, 2)]

gChief_x, gChief_y = 0, 0
gAssassin_x, gAssassin_y = 1, 0
gMilitant1_x, gMilitant1_y = 2, 0
gDiplomate_x, gDiplomate_y = 0, 1
gReporter_x, gReporter_y = 1, 1
gMilitant2_x, gMilitant2_y = 2, 1
gMilitant3_x, gMilitant3_y = 0, 2
gMilitant4_x, gMilitant4_y = 1, 2
gNecromobile_x, gNecromobile_y = 2, 2

green_locations = [(gChief_x, gChief_y), (gAssassin_x, gAssassin_y), (gMilitant1_x, gMilitant1_y),
                    (gDiplomate_x, gDiplomate_y), (gReporter_x, gReporter_y), (gMilitant2_x, gMilitant2_y),
                    (gMilitant3_x, gMilitant3_y), (gMilitant4_x, gMilitant4_y), (gNecromobile_x, gNecromobile_y)]

yellow_pieces = ['Militant', 'Assassin', 'Chief',
                 'Militant', 'Reporter', 'Diplomate',
                 'Necromobile', 'Militant', 'Militant']
# yellow_locations = [(6, 0), (7, 0), (8, 0),
#                     (6, 1), (7, 1), (8, 1),
#                     (6, 2), (7, 2), (8, 2)]

yMilitant1_x, yMilitant1_y = 6, 0
yAssassin_x, yAssassin_y = 7, 0
yChief_x, yChief_y = 8, 0
yMilitant2_x, yMilitant2_y = 6, 1
yReporter_x, yReporter_y = 7, 1
yDiplomate_x, yDiplomate_y = 8, 1
yNecromobile_x, yNecromobile_y = 6, 2
yMilitant3_x, yMilitant3_y = 7, 2
yMilitant4_x, yMilitant4_y = 8, 2

yellow_locations = [(yMilitant1_x, yMilitant1_y), (yAssassin_x, yAssassin_y), (yChief_x, yChief_y),
                    (yMilitant2_x, yMilitant2_y), (yReporter_x, yReporter_y), (yDiplomate_x, yDiplomate_y),
                    (yNecromobile_x, yNecromobile_y), (yMilitant3_x, yMilitant3_y), (yMilitant4_x, yMilitant4_y)]


red_pieces = ['Militant', 'Militant', 'Necromobile',
              'Diplomate', 'Reporter', 'Militant',
              'Chief', 'Assassin', 'Militant']
# red_locations = [(0, 6), (1, 6), (2, 6),
#                  (0, 7), (1, 7), (2, 7),
#                  (0, 8), (1, 8), (2, 8)]

rMilitant1_x, rMilitant1_y = 0, 6
rMilitant2_x, rMilitant2_y = 1, 6
rNecromobile_x, rNecromobile_y = 2, 6
rDiplomate_x, rDiplomate_y = 0, 7
rReporter_x, rReporter_y = 1, 7
rMilitant3_x, rMilitant3_y = 2, 7
rChief_x, rChief_y = 0, 8
rAssassin_x, rAssassin_y = 1, 8
rMilitant4_x, rMilitant4_y = 2, 8

red_locations = [(rMilitant1_x, rMilitant1_y), (rMilitant2_x, rMilitant2_y), (rNecromobile_x, rNecromobile_y),
                    (rDiplomate_x, rDiplomate_y), (rReporter_x, rReporter_y), (rMilitant3_x, rMilitant3_y),
                    (rChief_x, rChief_y), (rAssassin_x, rAssassin_y), (rMilitant4_x, rMilitant4_y)]



blue_pieces = ['Necromobile', 'Militant', 'Militant',
               'Militant', 'Reporter', 'Diplomate',
               'Militant', 'Assassin', 'Chief']
# blue_locations = [(6, 6), (7, 6), (8, 6),
#                   (6, 7), (7, 7), (8, 7),
#                   (6, 8), (7, 8), (8, 8)]

bNecromobile_x, bNecromobile_y = 6, 6
bMilitant1_x, bMilitant1_y = 7, 6
bMilitant2_x, bMilitant2_y = 8, 6
bMilitant3_x, bMilitant3_y = 6, 7
bReporter_x, bReporter_y = 7, 7
bDiplomate_x, bDiplomate_y = 8, 7
bMilitant4_x, bMilitant4_y = 6, 8
bAssassin_x, bAssassin_y = 7, 8
bChief_x, bChief_y = 8, 8

blue_locations = [(bNecromobile_x, bNecromobile_y), (bMilitant1_x, bMilitant1_y), (bMilitant2_x, bMilitant2_y),
                    (bMilitant3_x, bMilitant3_y), (bReporter_x, bReporter_y), (bDiplomate_x, bDiplomate_y),
                    (bMilitant4_x, bMilitant4_y), (bAssassin_x, bAssassin_y), (bChief_x, bChief_y)]

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
