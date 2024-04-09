import pygame
import constantes
import main
import ui

# Global variables
# Selected square by the user
selected_square = None
# Select pawn and stock it
selected_pawn = None
# Reporter targeting mode
reporter_targeting_mode = False
# Just moved reporter
just_moved_reporter = False
# Music playing
music_playing = True


class Board:
    def __init__(self):
        # Initialisation du plateau de jeu
        self.board = [
            ['green chief', 'green assassin', 'green militant', '', '', '', 'yellow militant', 'yellow assassin',
             'yellow chief'],
            ['green diplomate', 'green reporter', 'green militant', '', '', '', 'yellow militant', 'yellow reporter',
             'yellow diplomate'],
            ['green militant', 'green militant', 'green necromobile', '', '', '', 'yellow necromobile',
             'yellow militant', 'yellow militant'],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', 'laby', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['red militant', 'red militant', 'red necromobile', '', '', '', 'blue necromobile', 'blue militant',
             'blue militant'],
            ['red diplomate', 'red reporter', 'red militant', '', '', '', 'blue militant', 'blue reporter',
             'blue diplomate'],
            ['red chief', 'red assassin', 'red militant', '', '', '', 'blue militant', 'blue assassin', 'blue chief']
        ]

    def draw_board(self, screen):
        pygame.draw.rect(screen, constantes.color['BLACK'], (constantes.BOARD_WIDTH, 0, constantes.BOARD_WIDTH, constantes.BOARD_HEIGHT))

def main_menu(screen, background_image):
    running = True
    menu_background = pygame.image.load("assets/main_background.png")
    menu_background = pygame.transform.scale(menu_background, (constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Vérifiez si l'utilisateur a cliqué sur le bouton "Play"
                if main.button_play.rect.collidepoint(event.pos):
                    running = False

        # Effacez l'écran et dessinez le menu principal
        screen.blit(menu_background, (0, 0))
        screen.blit(main.text_surface,main.text_rect)

        main.button_play.draw(screen)
        main.button_quit.draw(screen)
        pygame.display.flip()

def redraw_screen(screen, board, teams, background_image, wanted_image, music_button_rect=None):
    global reporter_targeting_mode

    offset_x = int(constantes.SCREEN_WIDTH * constantes.PADDING)
    offset_y = (constantes.SCREEN_HEIGHT - constantes.GRID_HEIGHT) // 2

    # screen.blit(background_image, (0, 0))
    screen.blit(wanted_image, (constantes.SCREEN_WIDTH // 2, 0))

    board.draw_board(screen)
    ui.draw_grid_lines(screen)

    if selected_square is not None:
        selected_x = offset_x + selected_square[1] * constantes.SQUARE_SIZE
        selected_y = offset_y + selected_square[0] * constantes.SQUARE_SIZE
        pygame.draw.rect(screen, (150, 150, 150), (selected_x, selected_y, constantes.SQUARE_SIZE, constantes.SQUARE_SIZE))

    ui.draw_pieces(screen, teams)

    if selected_pawn is not None:
        ui.draw_possible_moves(screen, selected_pawn, offset_x, offset_y, teams)
        ui.draw_pawn_info(screen, selected_pawn, constantes.SCREEN_WIDTH // 2 + 20, 20)

    if selected_pawn and not reporter_targeting_mode:
        ui.draw_possible_moves(screen, selected_pawn, offset_x, offset_y, teams)

    if selected_pawn and reporter_targeting_mode:
        ui.draw_possible_targets(screen, selected_pawn, teams, offset_x, offset_y)
        ui.draw_pass_button(screen)

    # Draw music button
    ui.draw_music_button(screen, music_on=True)

    pygame.display.flip()

pygame.font.init()

