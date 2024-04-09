import pygame

import constantes
import ui
from Pawn.Subclass.Reporter import Reporter
from constantes import *


########################################
#                                      #
#             Draw Pieces              #
#                                      #
########################################


def draw_pieces(screen, teams):
    # Draw all pieces on the board
    for team in teams:
        for piece in team:
            draw_piece(screen, piece)


def draw_piece(screen, piece):
    # Use the same offsets as for the grid lines
    offset_x = int(SCREEN_WIDTH * PADDING)
    offset_y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

    # Position adjusted with offsets
    piece_x = offset_x + piece.position[0] * SQUARE_SIZE
    piece_y = offset_y + piece.position[1] * SQUARE_SIZE

    # Draw the background square for pawn
    # pygame.draw.rect(screen, piece.color, (piece_x, piece_y, SQUARE_SIZE, SQUARE_SIZE))

    # Load and resize pawn image
    piece_image = pygame.image.load(piece.image)
    resized_piece_image = pygame.transform.scale(piece_image, piece.scale)

    # Draw the image of the pawn in the adjusted position
    screen.blit(resized_piece_image,
                (piece_x + (SQUARE_SIZE - piece.scale[0]) // 2,
                 piece_y + (SQUARE_SIZE - piece.scale[1]) // 2))


########################################
#                                      #
#        Draw Possible Moves           #
#                                      #
########################################

def draw_possible_moves(screen, piece, offset_x, offset_y, teams):
    if piece is not None:
        possible_moves = piece.get_possible_moves(teams)
        for move in possible_moves:
            # Use the same offsets as for the grid lines
            x, y = move
            square_x = offset_x + x * SQUARE_SIZE
            square_y = offset_y + y * SQUARE_SIZE
            # Draw a circle in the center of the square
            pygame.draw.circle(screen, (255, 255, 0), (square_x + SQUARE_SIZE // 2, square_y + SQUARE_SIZE // 2), 10)


def draw_possible_targets(screen, reporter, teams, offset_x, offset_y):
    if reporter is not None and isinstance(reporter, Reporter):
        for direction in ["up", "down", "left", "right"]:
            adjacent_position = reporter.get_adjacent_position(direction)
            if reporter.can_kill(adjacent_position, teams):
                square_x = offset_x + adjacent_position[1] * constantes.SQUARE_SIZE
                square_y = offset_y + adjacent_position[0] * constantes.SQUARE_SIZE
                pygame.draw.circle(screen, (255, 0, 0),
                                   (square_x + constantes.SQUARE_SIZE // 2, square_y + constantes.SQUARE_SIZE // 2), 10)


########################################
#                                      #
#          Draw Grid Lines             #
#                                      #
########################################

def draw_grid_lines(screen):
    # Padding % with respect to the screen width
    offset_x = int(SCREEN_WIDTH * PADDING)
    offset_y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

    # Load and resize the crown image
    crown_image = pygame.image.load('assets/Crown.png')
    crown_image = pygame.transform.scale(crown_image, (SQUARE_SIZE, SQUARE_SIZE))

    # Draw labyrinth square
    for row in range(ROWS):
        for col in range(COLS):
            # Calculate the position of the square
            square_x = offset_x + col * SQUARE_SIZE
            square_y = offset_y + row * SQUARE_SIZE

            # Check if the current square is the labyrinth position
            if (row, col) == constantes.LABYRINTH_POSITION:
                # draw a crown on the labyrinth square
                screen.blit(crown_image, (square_x, square_y))

    # draw the grid lines
    for i in range(ROWS + 1):
        pygame.draw.line(screen, (155, 155, 155), (offset_x, offset_y + i * SQUARE_SIZE),
                         (offset_x + GRID_WIDTH, offset_y + i * SQUARE_SIZE))
        pygame.draw.line(screen, (155, 155, 155), (offset_x + i * SQUARE_SIZE, offset_y),
                         (offset_x + i * SQUARE_SIZE, offset_y + GRID_HEIGHT))


def draw_line(screen, i):
    # Draw a single line on the grid
    offset_percentage = 0.07
    adjusted_position_horizontal = int(GRID_WIDTH * offset_percentage)
    adjusted_position_vertical = int(GRID_HEIGHT * offset_percentage)
    pygame.draw.line(screen, (255, 0, 0), (adjusted_position_horizontal, i * SQUARE_SIZE),
                     (GRID_WIDTH + adjusted_position_horizontal, i * SQUARE_SIZE))
    pygame.draw.line(screen, (255, 0, 0), (i * SQUARE_SIZE + adjusted_position_horizontal, adjusted_position_vertical),
                     (i * SQUARE_SIZE + adjusted_position_horizontal, GRID_HEIGHT + adjusted_position_vertical))


########################################
#                                      #
#         Right Info Board             #
#                                      #
########################################

def draw_pass_button(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("Pass", True, (255, 255, 255))
    button_rect = text.get_rect(center=(constantes.SCREEN_WIDTH * 3 / 4, 20))
    pygame.draw.rect(screen, (0, 128, 0), button_rect.inflate(20, 10))
    screen.blit(text, button_rect)
    return button_rect


def draw_pawn_info(screen, pawn, x, y):
    if pawn is not None:
        font = pygame.font.Font(None, 50)

        # Calculate the middle point of the screen
        middle_point = SCREEN_WIDTH // 2 + SCREEN_WIDTH // 4

        # pygame.draw.rect(screen, (0, 0, 0), (middle_point, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT))

        # Loading the pawn image
        pawn_image = pygame.image.load(pawn.image)
        pawn_image = pygame.transform.scale(pawn_image, (SQUARE_SIZE * 2.2, SQUARE_SIZE * 2.2))
        image_x = middle_point - (SQUARE_SIZE * 2.2) // 2
        screen.blit(pawn_image, (image_x, SQUARE_SIZE))

        # Pawn information
        info_type = font.render(f"Type: {pawn.type}", True, (255, 255, 255))
        info_status = font.render(f"Status: {'Alive' if pawn.is_alive else 'Died'}", True, (255, 255, 255))

        # Calculate the position of the text
        text_x = middle_point - info_type.get_width() // 2
        y_text_start = SQUARE_SIZE * 3.6

        # Display the information on the screen
        screen.blit(info_type, (text_x, y_text_start))
        screen.blit(info_status, (text_x, y_text_start + 50))


def draw_current_player(screen, current_player):
    # Display the current player on the screen
    # Calculate the position of the text and font size
    font = pygame.font.Font(None, 50)
    y_text_start = SQUARE_SIZE * 0

    # Clear the previous text
    clear_rect = (0, y_text_start, SCREEN_WIDTH, font.get_height())
    pygame.draw.rect(screen, constantes.color['BLACK'], clear_rect)

    # Display the current player on the screen
    player_messages = {
        'RED': "Les enfants de Surtr attaque !",
        'BLUE': "Au tour des larbins d'Aquaman !",
        'GREEN': "Les disciples de la Terre se déchainent !",
        'YELLOW': "Les soldats d'Apophis se réveillent !"
    }

    player_text = player_messages.get(current_player.color)
    player_text_surface = font.render(player_text, True, constantes.color[current_player.color])

    text_x = SCREEN_WIDTH // 2 - player_text_surface.get_width() // 2
    screen.blit(player_text_surface, (text_x, y_text_start))


def draw_music_button(screen, music_on):
    font = pygame.font.Font(None, 36)
    text = font.render("Music", True, (255, 255, 255))
    button_rect = text.get_rect(center=(constantes.SCREEN_WIDTH - 50, constantes.SCREEN_HEIGHT - 20))
    pygame.draw.rect(screen, (0, 128, 0), button_rect.inflate(20, 10))
    screen.blit(text, button_rect)
    return button_rect
