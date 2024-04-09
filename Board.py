import pygame
import constantes
import ui


class Board:
    def __init__(self, game):
        self.game = game

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
        self.__draw_board()

    def __draw_board(self):
        pygame.draw.rect(self.game.screen, constantes.color['BLACK'], (constantes.BOARD_WIDTH, 0,
                                                                       constantes.BOARD_WIDTH, constantes.BOARD_HEIGHT))

    def redraw(self):
        self.__draw_board()

        offset_x = int(constantes.SCREEN_WIDTH * constantes.PADDING)
        offset_y = (constantes.SCREEN_HEIGHT - constantes.GRID_HEIGHT) // 2

        self.game.screen.blit(self.game.background_image, (0, 0))
        self.game.screen.blit(self.game.wanted_image, (constantes.SCREEN_WIDTH // 2, 0))

        ui.draw_grid_lines(self.game.screen)

        if self.game.selected_square is not None:
            selected_x = offset_x + self.game.selected_square[1] * constantes.SQUARE_SIZE
            selected_y = offset_y + self.game.selected_square[0] * constantes.SQUARE_SIZE
            pygame.draw.rect(self.game.screen, (150, 150, 150), (selected_x, selected_y,
                                                                 constantes.SQUARE_SIZE, constantes.SQUARE_SIZE))

        ui.draw_pieces(self.game.screen, self.game.teams)

        if self.game.selected_pawn is not None:
            ui.draw_possible_moves(self.game.screen, self.game.selected_pawn, offset_x, offset_y, self.game.teams)
            ui.draw_pawn_info(self.game.screen, self.game.selected_pawn, constantes.SCREEN_WIDTH // 2 + 20, 20)

        if self.game.selected_pawn and not self.game.reporter_targeting_mode:
            ui.draw_possible_moves(self.game.screen, self.game.selected_pawn, offset_x, offset_y, self.game.teams)

        if self.game.selected_pawn and self.game.reporter_targeting_mode:
            ui.draw_possible_targets(self.game.screen, self.game.selected_pawn, self.game.teams, offset_x, offset_y)
            ui.draw_pass_button(self.game.screen)

        # Draw music button
        ui.draw_music_button(self.game.screen, music_on=True)

        pygame.display.flip()


