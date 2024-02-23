import pygame


def get_screen_size():
    # Initialize pygame to get display information
    pygame.init()

    # Get the current display information
    display_info = pygame.display.Info()
    user_screen_width = display_info.current_w
    user_screen_height = display_info.current_h

    # Set the window size to 90% of the user's screen size
    window_percentage = 0.9
    window_width = int(user_screen_width * window_percentage)
    window_height = int(user_screen_height * window_percentage)

    # Quit pygame init to avoid interference with the main game loop init
    pygame.quit()

    return window_width, window_height


# Call the function and set the constants
SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_size()

# Board dimensions
BOARD_WIDTH, BOARD_HEIGHT = SCREEN_WIDTH // 2, SCREEN_HEIGHT

# Grid dimensions for the game
GRID_WIDTH, GRID_HEIGHT = BOARD_WIDTH * 0.85, BOARD_HEIGHT * 0.85

# Number of rows and columns on the grid
ROWS, COLS = 9, 9

# Size of a single square on the grid
SQUARE_SIZE = int((GRID_WIDTH // ROWS) * 0.95)

# Recalculez GRID_WIDTH et GRID_HEIGHT en fonction du nouveau SQUARE_SIZE
GRID_WIDTH = SQUARE_SIZE * ROWS
GRID_HEIGHT = SQUARE_SIZE * COLS

# Padding of screen width for the grid, the board and pawns
PADDING = 0.053

# Colors used in the game
color = {
    'RED': (255, 87, 87),
    'BLUE': (87, 154, 255),
    'GREEN': (161, 255, 87),
    'YELLOW': (255, 228, 87),
    'GREY': (203, 203, 203),
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255)
}

# Game's FPS
FPS = 60

# Images for the pieces
ASSASSIN_IMAGE = './assets/assassin-150x150.png'
REPORTER_IMAGE = './assets/reporter-150x150.png'
DIPLOMAT_IMAGE = './assets/diplomate-150x150.png'
NECROMOBILE_IMAGE = './assets/necromobile-150x150.png'
CHIEF_IMAGE = './assets/chef-150x150.png'
MILITANT_IMAGE = './assets/militant-150x150.png'

# Images for the board
BOARD_BACKGROUND = './assets/board.png'
