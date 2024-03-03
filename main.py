import constantes
from constantes import *
from Board import Board
from Pawn import Assassin, Reporter, Chief, Militant, Diplomat, Necromobile

# Global variables
# Selected square by the user
selected_square = None
# Select pawn and stock it
selected_pawn = None


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
        pygame.draw.line(screen, (155, 155, 155), (offset_x, offset_y + i * SQUARE_SIZE), (offset_x + GRID_WIDTH, offset_y + i * SQUARE_SIZE))
        pygame.draw.line(screen, (155, 155, 155), (offset_x + i * SQUARE_SIZE, offset_y), (offset_x + i * SQUARE_SIZE, offset_y + GRID_HEIGHT))


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


def draw_line(screen, i):
    # Draw a single line on the grid
    offset_percentage = 0.07
    adjusted_position_horizontal = int(GRID_WIDTH * offset_percentage)
    adjusted_position_vertical = int(GRID_HEIGHT * offset_percentage)
    pygame.draw.line(screen, (255, 0, 0), (adjusted_position_horizontal, i * SQUARE_SIZE),
                     (GRID_WIDTH + adjusted_position_horizontal, i * SQUARE_SIZE))
    pygame.draw.line(screen, (255, 0, 0), (i * SQUARE_SIZE + adjusted_position_horizontal, adjusted_position_vertical),
                     (i * SQUARE_SIZE + adjusted_position_horizontal, GRID_HEIGHT + adjusted_position_vertical))


def draw_pawn_info(screen, pawn, x, y):
    if pawn is not None:
        # Font for the information
        font = pygame.font.Font(None, 50)

        # Calculate the middle point of the screen
        middle_point = SCREEN_WIDTH // 2 + SCREEN_WIDTH // 4

        # Loading the pawn image
        pawn_image = pygame.image.load(pawn.image)
        pawn_image = pygame.transform.scale(pawn_image, (SQUARE_SIZE * 2.2, SQUARE_SIZE * 2.2))
        image_x = middle_point - (SQUARE_SIZE * 2.2) // 2
        screen.blit(pawn_image, (image_x, SQUARE_SIZE))

        # Pawn information
        y_text_start = SQUARE_SIZE * 3.6
        info_type = font.render(f"Type: {pawn.type}", True, (255, 255, 255))
        info_status = font.render(f"Status: {'Alive' if pawn.is_alive else 'Died'}", True, (255, 255, 255))

        # Calculate the position of the text
        text_x = middle_point - info_type.get_width() // 2

        # Display the information on the screen
        screen.blit(info_type, (text_x, y_text_start))
        screen.blit(info_status, (text_x, y_text_start + 50))


def game_loop(screen, board, teams, background_image):
    global selected_square, selected_pawn

    # Main game loop
    running = True
    clock = pygame.time.Clock()
    needs_redraw = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(event, teams, screen, background_image, board)
                # Redraw the screen after a click
                redraw_screen(screen, board, teams, background_image)
                needs_redraw = False

        if needs_redraw:
            redraw_screen(screen, board, teams, background_image)
            needs_redraw = False

        clock.tick(FPS)


def redraw_screen(screen, board, teams, background_image):
    offset_x = int(SCREEN_WIDTH * PADDING)
    offset_y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

    screen.blit(background_image, (0, 0))
    draw_board(screen, board)
    draw_grid_lines(screen)

    if selected_square is not None:
        selected_x = offset_x + selected_square[1] * SQUARE_SIZE
        selected_y = offset_y + selected_square[0] * SQUARE_SIZE
        pygame.draw.rect(screen, (150, 150, 150), (selected_x, selected_y, SQUARE_SIZE, SQUARE_SIZE))

    draw_pieces(screen, teams)

    if selected_pawn is not None:
        draw_possible_moves(screen, selected_pawn, offset_x, offset_y, teams)
        draw_pawn_info(screen, selected_pawn, SCREEN_WIDTH // 2 + 20, 20)

    pygame.display.flip()


pygame.font.init()


def handle_mouse_click(event, teams, screen, background_image, board):
    # Modify the global variable selected_square and selected_pawn
    global selected_square, selected_pawn

    # Handle mouse click events
    offset_x = int(SCREEN_WIDTH * PADDING)
    offset_y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2
    pos = pygame.mouse.get_pos()
    # Adjust mouse position to account for offsets
    adjusted_x = pos[0] - offset_x
    adjusted_y = pos[1] - offset_y
    # Calculate the row and column, taking the offsets into account
    row = adjusted_y // SQUARE_SIZE
    col = adjusted_x // SQUARE_SIZE
    print(col, row)

    # if a pawn is selected, move it to the new position
    if selected_pawn:
        new_position = (col, row)
        if selected_pawn.can_move(new_position, teams):
            selected_pawn.move(new_position, teams)
            selected_square = None
            selected_pawn = None
        else:
            # if the move is not valid, reset the selected pawn and square
            selected_pawn = None
            selected_square = None
    else:
        # verify if a pawn is present on the selected square
        for team in teams:
            for piece in team:
                if piece.position == (col, row):
                    selected_pawn = piece
                    selected_square = (row, col)
                    break

    screen.blit(background_image, (0, 0))
    draw_board(screen, board)
    draw_pieces(screen, teams)
    draw_grid_lines(screen)
    pygame.display.flip()


def main():
    screen, background_image = init_pygame()
    board = Board()
    teams = create_teams()
    screen.blit(background_image, (0, 0))
    draw_board(screen, board)
    draw_pieces(screen, teams)
    draw_grid_lines(screen)
    pygame.display.flip()
    game_loop(screen, board, teams, background_image)


if __name__ == "__main__":
    main()
