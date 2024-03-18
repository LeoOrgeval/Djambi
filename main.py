from constantes import *
from Board import Board
from Pawn import Assassin, Reporter, Chief, Militant, Diplomat, Necromobile
from ui import *

# Global variables
# Selected square by the user
selected_square = None
# Select pawn and stock it
selected_pawn = None
# Reporter targeting mode
reporter_targeting_mode = False
# Just moved reporter
just_moved_reporter = False


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
    global reporter_targeting_mode

    offset_x = int(SCREEN_WIDTH * PADDING)
    offset_y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

    screen.blit(background_image, (0, 0))
    board.draw_board(screen)
    draw_grid_lines(screen)

    if selected_square is not None:
        selected_x = offset_x + selected_square[1] * SQUARE_SIZE
        selected_y = offset_y + selected_square[0] * SQUARE_SIZE
        pygame.draw.rect(screen, (150, 150, 150), (selected_x, selected_y, SQUARE_SIZE, SQUARE_SIZE))

    draw_pieces(screen, teams)

    if selected_pawn is not None:
        draw_possible_moves(screen, selected_pawn, offset_x, offset_y, teams)
        draw_pawn_info(screen, selected_pawn, SCREEN_WIDTH // 2 + 20, 20)

    if selected_pawn and not reporter_targeting_mode:
        draw_possible_moves(screen, selected_pawn, offset_x, offset_y, teams)

    if selected_pawn and reporter_targeting_mode:
        draw_possible_targets(screen, selected_pawn, teams, offset_x, offset_y)
        draw_pass_button(screen)

    pygame.display.flip()


pygame.font.init()


def handle_mouse_click(event, teams, screen, background_image, board):
    global selected_square, selected_pawn, reporter_targeting_mode, just_moved_reporter

    offset_x = int(SCREEN_WIDTH * PADDING)
    offset_y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2
    pos = pygame.mouse.get_pos()
    adjusted_x = pos[0] - offset_x
    adjusted_y = pos[1] - offset_y
    row = adjusted_y // SQUARE_SIZE
    col = adjusted_x // SQUARE_SIZE

    if reporter_targeting_mode:
        pass_button_rect = draw_pass_button(screen)

        if isinstance(selected_pawn, Reporter):

            if selected_pawn.can_kill((row, col), teams):
                selected_pawn.kill_adjacent_pawn((row, col), teams)
            reporter_targeting_mode = False
            just_moved_reporter = False
            redraw_screen(screen, board, teams, background_image)
            return

        if pass_button_rect.collidepoint(pos):
            reporter_targeting_mode = False
            just_moved_reporter = False
            redraw_screen(screen, board, teams, background_image)
            return

        return

    if selected_pawn and selected_pawn.is_alive:
        new_position = (col, row)
        if selected_pawn.can_move(new_position, teams):
            selected_pawn.move(new_position, teams)
            just_moved_reporter = isinstance(selected_pawn, Reporter)
            if just_moved_reporter:
                draw_possible_targets(screen, selected_pawn, teams, offset_x, offset_y)
                draw_pass_button(screen)
                reporter_targeting_mode = True
            else:
                reporter_targeting_mode = False
            selected_square = None
            selected_pawn = None
            redraw_screen(screen, board, teams, background_image)
            return
        else:

            selected_pawn = None
            selected_square = None
            just_moved_reporter = False
            reporter_targeting_mode = False

    else:

        for team in teams:
            for piece in team:
                if piece.position == (col, row) and piece.is_alive:
                    selected_pawn = piece
                    selected_square = (row, col)
                    break

    redraw_screen(screen, board, teams, background_image)


def main():
    screen, background_image = init_pygame()
    board = Board()
    board.draw_board(screen)
    teams = create_teams()
    screen.blit(background_image, (0, 0))
    draw_pieces(screen, teams)
    draw_grid_lines(screen)
    pygame.display.flip()
    game_loop(screen, board, teams, background_image)


if __name__ == "__main__":
    main()
