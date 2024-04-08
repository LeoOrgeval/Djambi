import pygame
from pygame import surface, mixer
from pygame.mixer import music
from pygame.font import Font

import game
import constantes
import Board
import Players
import ui
import button

pygame.init()
# Title of the game
text_surface = pygame.font.Font(constantes.MYFONT, 30).render('Djambi Game', False, constantes.color['BLACK'])
text_rect = text_surface.get_rect(center=(constantes.SCREEN_WIDTH // 2, 50))

# Button
button_play = button.MiddleButton((200, 50), "Play")
button_quit = button.MiddleButton((200, 50), "Quit", (0, 75))

# Sound
mixer.init()
sound = music.load("assets/jurassic_park.mp3")
mixer.music.set_volume(1)
mixer.music.play()

button_volume_on = button.VolumeButton((50, 50), "ON")
button_volume_off = button.VolumeButton((50, 50), "OFF")
screen = pygame.display.set_mode([constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT], pygame.NOFRAME)

button_volume_on.draw(screen)

def main():
    screen, background_image, wanted_image = game.init_pygame()
    Board.main_menu(screen, background_image)

    # Init the game
    board = Board()
    board.draw_board(screen)
    music_button_rect = ui.draw_music_button(screen, music_on=True)
    teams = Players.create_teams()
    screen.blit(background_image, (0, 0))
    screen.blit(wanted_image, (constantes.SCREEN_WIDTH//2, 0))
    ui.draw_pieces(screen, teams)
    ui.draw_grid_lines(screen)
    pygame.display.flip()
    game.game_loop(screen, board, teams, background_image, wanted_image, music_button_rect)


if __name__ == "__main__":
    main()