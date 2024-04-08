import sys
import Players
import Board
import pygame
from pygame import surface, mixer
from pygame.mixer import music

from constantes import *


from ui import *
import button

pygame.init()






def init_pygame():
    # Initialize pygame and return the screen object
    pygame.init()

    # Use pygame.NOFRAME to remove the window border and fix bug with display when user ALT+TAB (Black screen)
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.NOFRAME)
    pygame.display.set_caption("Djambi")
    # Load background image and resize it to fit the first half screen
    background_image = pygame.image.load(BOARD_BACKGROUND)
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
    wanted_image = pygame.image.load(WANTED_BACKGROUND)
    wanted_image = pygame.transform.scale(wanted_image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
    return screen, background_image, wanted_image

def game_loop(screen, board, teams, background_image, wanted_image, music_button_rect):
    global selected_square, selected_pawn, music_playing

    music.load('assets/test.mp3')
    # -1 means loop indefinitely
    music.play(-1)

    # Main game loop
    running = True
    clock = pygame.time.Clock()
    needs_redraw = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Players.handle_mouse_click(teams, screen, background_image, wanted_image, board)
                if music_button_rect.collidepoint(event.pos):
                    music_playing = not music_playing
                    if music_playing:
                        music.play(-1)
                    else:
                        music.stop()
                # Redraw the screen after a click
                Board.redraw_screen(screen, board, teams, background_image, wanted_image, music_button_rect)
                needs_redraw = False

        if needs_redraw:
            Board.redraw_screen(screen, board, teams, background_image, wanted_image, music_button_rect)
            needs_redraw = False

        clock.tick(FPS)

