import pygame
import constantes
import ui
import Board

from Pawn.Subclass.Chief import Chief
from Pawn.Subclass.Reporter import Reporter
from Pawn.Subclass.Assassin import Assassin
from Pawn.Subclass.Diplomat import Diplomat
from Pawn.Subclass.Militant import Militant
from Pawn.Subclass.Necromobile import Necromobile

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

def handle_mouse_click(teams, screen, background_image, wanted_image, board):
    global selected_square, selected_pawn, reporter_targeting_mode, just_moved_reporter

    offset_x = int(constantes.SCREEN_WIDTH * constantes.PADDING)
    offset_y = (constantes.SCREEN_HEIGHT - constantes.GRID_HEIGHT) // 2
    pos = pygame.mouse.get_pos()
    adjusted_x = pos[0] - offset_x
    adjusted_y = pos[1] - offset_y
    row = adjusted_y // constantes.SQUARE_SIZE
    col = adjusted_x // constantes.SQUARE_SIZE

    # Check if the music button is clicked
    # if music_button_rect.collidepoint(pos):
    #     # Need help toggle music sound on off or on on when click the button:
    #     pass

    if reporter_targeting_mode:
        pass_button_rect = ui.draw_pass_button(screen)

        if isinstance(selected_pawn, Reporter):

            if selected_pawn.can_kill((row, col), teams):
                selected_pawn.kill_adjacent_pawn((row, col), teams)
            reporter_targeting_mode = False
            just_moved_reporter = False
            Board.redraw_screen(screen, board, teams, background_image, wanted_image)
            return

        if pass_button_rect.collidepoint(pos):
            reporter_targeting_mode = False
            just_moved_reporter = False
            Board.redraw_screen(screen, board, teams, background_image, wanted_image)
            return

        return

    if selected_pawn and selected_pawn.is_alive:
        new_position = (col, row)
        if selected_pawn.can_move(new_position, teams):
            selected_pawn.move(new_position, teams)
            just_moved_reporter = isinstance(selected_pawn, Reporter)
            if just_moved_reporter:
                ui.draw_possible_targets(screen, selected_pawn, teams, offset_x, offset_y)
                ui.draw_pass_button(screen)
                reporter_targeting_mode = True
            else:
                reporter_targeting_mode = False
            selected_square = None
            selected_pawn = None
            Board.redraw_screen(screen, board, teams, background_image, wanted_image)
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

    Board.redraw_screen(screen, board, teams, background_image, wanted_image)
