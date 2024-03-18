import pygame
from constantes import *


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.green_pieces = ['Chief', 'Assassin', 'Militant',
                             'Diplomate', 'Reporter', 'Militant',
                             'Militant', 'Militant', 'Necromobile']
        self.green_locations = [(0, 0), (1, 0), (2, 0),
                                (0, 1), (1, 1), (2, 1),
                                (0, 2), (1, 2), (2, 2)]

        self.yellow_pieces = ['Militant', 'Assassin', 'Chief',
                              'Militant', 'Reporter', 'Diplomate',
                              'Necromobile', 'Militant', 'Militant']
        self.yellow_locations = [(6, 0), (7, 0), (8, 0),
                                 (6, 1), (7, 1), (8, 1),
                                 (6, 2), (7, 2), (8, 2)]

        self.red_pieces = ['Militant', 'Militant', 'Necromobile',
                           'Diplomate', 'Reporter', 'Militant',
                           'Chief', 'Assassin', 'Militant']
        self.red_locations = [(0, 6), (1, 6), (2, 6),
                              (0, 7), (1, 7), (2, 7),
                              (0, 8), (1, 8), (2, 8)]

        self.blue_pieces = ['Necromobile', 'Militant', 'Militant',
                            'Militant', 'Reporter', 'Diplomate',
                            'Militant', 'Assassin', 'Chief']
        self.blue_locations = [(6, 6), (7, 6), (8, 6),
                               (6, 7), (7, 7), (8, 7),
                               (6, 8), (7, 8), (8, 8)]

        self.pieces_image = {
            'Chief': pygame.transform.scale(pygame.image.load('assets/chef-150x150.png'), (57, 57)),
            'Assassin': pygame.transform.scale(pygame.image.load('assets/assassin-150x150.png'), (57, 57)),
            'Diplomate': pygame.transform.scale(pygame.image.load('assets/diplomate-150x150.png'), (57, 57)),
            'Reporter': pygame.transform.scale(pygame.image.load('assets/reporter-150x150.png'), (57, 57)),
            'Necromobile': pygame.transform.scale(pygame.image.load('assets/necromobile-150x150.png'), (57, 57)),
            'Militant': pygame.transform.scale(pygame.image.load('assets/militant-150x150.png'), (57, 57))
        }
        self.pieces_list = ['Chief', 'Assassin', 'Reporter', 'Necromobile', 'Diplomate', 'Militant']

    def display(self):
        # dessiner un fond blanc entre le plateau (700x700) et un fond noir pour le reste de la fenêtre (1400x700)
        self.screen.fill(WHITE)
        pygame.draw.rect(self.screen, BLACK, (WIDTH, 0, WIDTH, HEIGHT))

        # Dessiner les pièces
        self.display_pieces()

        # Dessiner les lignes de la grille
        for i in range(1, ROWS):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE))
            pygame.draw.line(self.screen, (0, 0, 0), (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT))

    def display_pieces(self):
        for pieces, locations, color in [(self.green_pieces, self.green_locations, GREEN),
                                         (self.yellow_pieces, self.yellow_locations, YELLOW),
                                         (self.red_pieces, self.red_locations, RED),
                                         (self.blue_pieces, self.blue_locations, BLUE)]:
            for i in range(len(pieces)):
                piece = pieces[i]
                x, y = locations[i]
                piece_image = self.pieces_image[piece]
                pygame.draw.rect(self.screen, color, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                self.screen.blit(piece_image, (x * SQUARE_SIZE + 10, y * SQUARE_SIZE + 10))
