from constantes import *
from Board import Board
from Pawn import Assassin, Reporter, Chief, Militant, Diplomat, Necromobile


def init_pygame():
    # Initialize pygame and return the screen object
    pygame.init()

    # Use pygame.NOFRAME to remove the window border and fix bug with display when user ALT+TAB (Black screen)
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.NOFRAME)
    pygame.display.set_caption("Djambi")
    # Load background image and resize it to fit the first half screen
    background_image = pygame.image.load(BOARD_BACKGROUND)
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
    return screen, background_image


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


def draw_grid_lines(screen):
    # Padding % of screen width
    offset_x = int(SCREEN_WIDTH * PADDING)
    # To center grid vertically
    offset_y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

    # Draw the grid lines
    for i in range(ROWS + 1):
        # Horizontal line
        pygame.draw.line(screen, (255, 0, 0), (offset_x, offset_y + i * SQUARE_SIZE),
                         (offset_x + GRID_WIDTH, offset_y + i * SQUARE_SIZE))
        # Vertical line
        pygame.draw.line(screen, (255, 0, 0), (offset_x + i * SQUARE_SIZE, offset_y),
                         (offset_x + i * SQUARE_SIZE, offset_y + GRID_HEIGHT))


def draw_piece(screen, piece):
    # Use the same offsets as for the grid lines
    offset_x = int(SCREEN_WIDTH * PADDING)
    offset_y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

    # Position adjusted with offsets
    piece_x = offset_x + piece.position[0] * SQUARE_SIZE
    piece_y = offset_y + piece.position[1] * SQUARE_SIZE

    # Draw the background square for pawn
    pygame.draw.rect(screen, piece.color, (piece_x, piece_y, SQUARE_SIZE, SQUARE_SIZE))

    # Load and resize pawn image
    piece_image = pygame.image.load(piece.image)
    resized_piece_image = pygame.transform.scale(piece_image, piece.scale)

    # Draw the image of the pawn in the adjusted position
    screen.blit(resized_piece_image,
                (piece_x + (SQUARE_SIZE - piece.scale[0]) // 2,
                 piece_y + (SQUARE_SIZE - piece.scale[1]) // 2))


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
    offset_x = int(SCREEN_WIDTH * PADDING)
    offset_y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

    pos = pygame.mouse.get_pos()

    # Adjust mouse position to account for offsets
    adjusted_x = pos[0] - offset_x
    adjusted_y = pos[1] - offset_y

    # Ensure that clicks outside the grid are ignored
    if adjusted_x < 0 or adjusted_y < 0 or adjusted_x >= GRID_WIDTH or adjusted_y >= GRID_HEIGHT:
        return

    # Calculate the row and column, taking the offsets into account
    row = adjusted_y // SQUARE_SIZE
    col = adjusted_x // SQUARE_SIZE
    print(col, row)


def main():
    screen, background_image = init_pygame()
    board = Board()
    teams = create_teams()
    screen.blit(background_image, (0, 0))
    draw_board(screen, board)
    draw_pieces(screen, teams)
    draw_grid_lines(screen)
    pygame.display.flip()
    game_loop(screen, board, teams)


if __name__ == "__main__":
    main()
