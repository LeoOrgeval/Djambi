import pygame
from constantes import *
from Board import Board
from Pawn import Assassin, Reporter, Chief, Militant, Diplomat, Necromobile


def init_pygame():
    # Initialize pygame and return the screen object
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("Djambi")
    return screen


def create_teams():
    # Create all teams and return them in a list
    teams = []
    colors = ['green', 'yellow', 'red', 'blue']
    for color in colors:
        team = [Diplomat(color), Chief(color), Assassin(color), Reporter(color)] + \
               [Militant(color, i) for i in range(4)] + \
               [Necromobile(color)]
        teams.append(team)
    return teams


def draw_board(screen, board):
    # Draw the game board and the background
    pygame.draw.rect(screen, color['BLACK'], (BOARD_WIDTH, 0, BOARD_WIDTH, BOARD_HEIGHT))
    board.display_board()


def draw_pieces(screen, teams):
    # Draw all pieces on the board
    for team in teams:
        for piece in team:
            draw_piece(screen, piece)


def draw_piece(screen, piece):
    # Draw a single piece on the board

    print("Color:", piece.color)
    print("Position:", piece.position)

    pygame.draw.rect(screen, piece.color, (piece.position[0] * SQUARE_SIZE, piece.position[1] * SQUARE_SIZE,
                                           SQUARE_SIZE, SQUARE_SIZE))
    piece_image = pygame.image.load(piece.image)
    resized_piece_image = pygame.transform.scale(piece_image, piece.scale)
    screen.blit(resized_piece_image,
                (piece.position[0] * SQUARE_SIZE + (SQUARE_SIZE - piece.scale[0]) // 2,
                 piece.position[1] * SQUARE_SIZE + (SQUARE_SIZE - piece.scale[1]) // 2))


def draw_grid_lines(screen):
    # Draw the grid lines on the board
    for i in range(1, ROWS):
        draw_line(screen, i)


def draw_line(screen, i):
    # Draw a single line on the grid
    offset_percentage = 0.07
    adjusted_position_horizontal = int(GRID_WIDTH * offset_percentage)
    adjusted_position_vertical = int(GRID_HEIGHT * offset_percentage)
    pygame.draw.line(screen, (255, 0, 0), (adjusted_position_horizontal, i * SQUARE_SIZE),
                     (GRID_WIDTH + adjusted_position_horizontal, i * SQUARE_SIZE))
    pygame.draw.line(screen, (255, 0, 0), (i * SQUARE_SIZE + adjusted_position_horizontal, adjusted_position_vertical),
                     (i * SQUARE_SIZE + adjusted_position_horizontal, GRID_HEIGHT + adjusted_position_vertical))


def game_loop(screen, board, teams):
    # Main game loop
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(event)
        pygame.display.flip()
        clock.tick(FPS)


def handle_mouse_click(event):
    # Handle mouse click events
    pos = pygame.mouse.get_pos()
    row = pos[1] // SQUARE_SIZE
    col = pos[0] // SQUARE_SIZE
    print(row, col)


def main():
    screen = init_pygame()
    board = Board()
    teams = create_teams()
    draw_board(screen, board)
    draw_pieces(screen, teams)
    draw_grid_lines(screen)
    pygame.display.flip()
    game_loop(screen, board, teams)


if __name__ == "__main__":
    main()
