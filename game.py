import Pawn
import Board
import button
import random
from pygame.mixer import music
from pygame import mixer

import ui
from ui import *
from Pawn.Subclass.Chief import Chief
from Pawn.Subclass.Reporter import Reporter
from Pawn.Subclass.Assassin import Assassin
from Pawn.Subclass.Diplomat import Diplomat
from Pawn.Subclass.Militant import Militant
from Pawn.Subclass.Necromobile import Necromobile
from Players import Player


class Game:
    screen: pygame.SurfaceType
    background_image: pygame.SurfaceType
    wanted_image: pygame.SurfaceType
    teams: list
    reporter_targeting_mode: bool = False
    selected_square: tuple = None
    selected_pawn: Pawn.Pawn = None
    just_moved_reporter: bool = False

    def __init__(self):
        # Initialize pygame
        pygame.init()
        pygame.display.set_caption("Djambi")

        # Use pygame.NOFRAME to remove the window border and fix bug with display when user ALT+TAB (Black screen)
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.NOFRAME)

        # Load the players and create the teams
        self.players = Player.create_players()
        random.shuffle(self.players)
        self.current_player_index = 0
        self.__create_teams()

        # Load background image and resize it to fit the first half screen
        background_image = pygame.image.load(BOARD_BACKGROUND)
        self.background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
        wanted_image = pygame.image.load(WANTED_BACKGROUND)
        self.wanted_image = pygame.transform.scale(wanted_image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
        self.__create_teams()
        self.board = Board.Board(self)
        self.music_button_rect = draw_music_button(self.screen, music_on=True)
        self.needs_redraw = False

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.display_current_player()

    def display_current_player(self):
        current_player = self.players[self.current_player_index]
        pygame.display.flip()

    def __create_teams(self):
        self.teams = []

        for player in self.players:
            color = player.color.lower()
            team = [Diplomat(color), Chief(color), Assassin(color), Reporter(color)] + \
                   [Militant(color, i) for i in range(4)] + \
                   [Necromobile(color)]
            self.teams.append(team)

    def load_main_menu(self):
        """
        Load the game interface for launching the game.
        :return:
        """
        # Title of the game
        text_surface = pygame.font.Font(constantes.MYFONT, 30).render('Djambi Game', False, constantes.color['BLACK'])
        text_rect = text_surface.get_rect(center=(constantes.SCREEN_WIDTH // 2, 50))

        # Button
        button_play = button.MiddleButton((200, 50), "Play")
        button_quit = button.MiddleButton((200, 50), "Quit", (0, 75))

        # Sound
        mixer.init()
        sound = music.load("assets/main_menu_song.mp3")
        mixer.music.set_volume(1)
        mixer.music.play()

        button_volume_on = button.VolumeButton((50, 50), "ON")
        button_volume_off = button.VolumeButton((50, 50), "OFF")
        screen = pygame.display.set_mode([constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT], pygame.NOFRAME)

        button_volume_on.draw(screen)
        running = True
        clock = pygame.time.Clock()

        menu_background = pygame.image.load("assets/main_background.png")
        menu_background = pygame.transform.scale(menu_background, (constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_play.is_clicked(event):
                        running = False
                        self.load()
                    if button_quit.is_clicked(event):
                        running = False

            # Effacez l'écran et dessinez le menu principal
            screen.blit(menu_background, (0, 0))
            screen.blit(text_surface, text_rect)

            button_play.draw(screen)
            button_quit.draw(screen)
            pygame.display.flip()

            clock.tick(FPS)

    def load(self):
        """
        Load the real game .
        :return:
        """
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.wanted_image, (constantes.SCREEN_WIDTH // 2, 0))
        draw_pieces(self.screen, self.teams)
        draw_grid_lines(self.screen)
        self.board.redraw()
        pygame.display.flip()
        self.display_current_player()
        self.game_loop()

    def game_loop(self):
        music.load('assets/game_song.mp3')
        music.set_volume(0.3)
        # -1 means loop indefinitely
        music.play(-1)

        # Main game loop
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__handle_mouse_click()
                    # Players.handle_mouse_click(self.teams, self.screen, self.background_image, self.wanted_image, self.board)
                    if self.music_button_rect.collidepoint(event.pos):
                        music_playing = not music_playing
                        if music_playing:
                            music.play(-1)
                        else:
                            music.stop()

                    # Redraw the screen after a click
                    self.board.redraw()
                    # Board.redraw_screen(screen, board, teams, background_image, wanted_image, music_button_rect)
                    self.needs_redraw = False
            ui.draw_current_player(self.screen, self.players[self.current_player_index])
            pygame.display.flip()
        if self.needs_redraw:
            self.board.redraw()
            self.needs_redraw = False

        clock.tick(FPS)

    def __handle_mouse_click(self):
        offset_x = int(constantes.SCREEN_WIDTH * constantes.PADDING)
        offset_y = (constantes.SCREEN_HEIGHT - constantes.GRID_HEIGHT) // 2
        pos = pygame.mouse.get_pos()
        adjusted_x = pos[0] - offset_x
        adjusted_y = pos[1] - offset_y
        row = adjusted_y // constantes.SQUARE_SIZE
        col = adjusted_x // constantes.SQUARE_SIZE

        current_player = self.players[self.current_player_index]

        # Check if the music button is clicked
        # if music_button_rect.collidepoint(pos):
        #     # Need help toggle music sound on off or on on when click the button:
        #     pass

        if self.reporter_targeting_mode:
            print("Reporter targeting mode")
            pass_button_rect = draw_pass_button(self.screen)

            if isinstance(self.selected_pawn, Reporter) and self.selected_pawn.color == current_player.color.lower():
                print("Reporter is selected")
                if self.selected_pawn.can_kill((row, col), self.teams):
                    print("Reporter can kill")
                    self.selected_pawn.kill_adjacent_pawn((row, col), self.teams)
                    self.next_player()
                self.reporter_targeting_mode = False
                self.just_moved_reporter = False
                self.board.redraw()
                return

            if pass_button_rect.collidepoint(pos):
                self.reporter_targeting_mode = False
                self.just_moved_reporter = False
                self.board.redraw()
                return

        if self.selected_pawn and self.selected_pawn.is_alive:
            # print(f"Couleur du pion sélectionné : {self.selected_pawn.color}")
            if self.selected_pawn.color == constantes.color[current_player.color]:
                new_position = (col, row)
                if new_position in self.selected_pawn.get_possible_moves(self.teams):
                    self.selected_pawn.move(new_position, self.teams)
                    just_moved_reporter = isinstance(self.selected_pawn, Reporter)
                    if just_moved_reporter:
                        draw_possible_targets(self.screen, self.selected_pawn, self.teams, offset_x, offset_y)
                        draw_pass_button(self.screen)
                        self.reporter_targeting_mode = True
                    else:
                        self.next_player()
                    self.selected_square = None
                    self.selected_pawn = None
                else:
                    self.selected_pawn = None
                    self.selected_square = None
                    self.just_moved_reporter = False
                    self.reporter_targeting_mode = False
                    # print("Ce n'est pas le tour de ce joueur")

        else:
            for team in self.teams:
                for piece in team:
                    if piece.position == (col, row) and piece.is_alive:
                        piece_color_rgb = constantes.color[current_player.color]
                        if piece.color == piece_color_rgb:
                            self.selected_pawn = piece
                            self.selected_square = (row, col)
                            # print("Pion sélectionné")
                            return
                        else:
                            print("Pion trouvé, mais pas de la bonne couleur")
                            self.display_current_player()

        self.board.redraw()
