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

# dessiner un fond blanc
screen.fill((255, 255, 255))

# dessiner le plateau
board.display_board()

# Dessiner les lignes de la grille
for i in range(1, ROWS+1):
    pygame.draw.line(screen, (0, 0, 0), (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE))
    pygame.draw.line(screen, (0, 0, 0), (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT))

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
chief = pygame.transform.scale(chief, (60,60))
assassin = pygame.image.load('assets/assassin-150x150.png')
assassin = pygame.transform.scale(assassin, (60,60))
diplomate = pygame.image.load('assets/diplomate-150x150.png')
diplomate = pygame.transform.scale(diplomate, (60,60))
reporter = pygame.image.load('assets/reporter-150x150.png')
reporter = pygame.transform.scale(reporter, (60,60))
necromobile = pygame.image.load('assets/necromobile-150x150.png')
necromobile = pygame.transform.scale(necromobile, (60,60))
militant = pygame.image.load('assets/militant-150x150.png')
militant = pygame.transform.scale(militant, (60,60))
maze = pygame.image.load('assets/chef-150x150.png')
maze = pygame.transform.scale(maze, (60,60))

pieces_image = [chief, assassin, reporter, necromobile, diplomate, militant]
pieces_list = ['Chief', 'Assassin', 'Reporter', 'Necromobile', 'Diplomate', 'Militant']

# Afficher les pièces

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
