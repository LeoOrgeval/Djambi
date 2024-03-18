from pygame import mixer
import pygame
import classes.Button
import constants
import fontawesome as fa

pygame.init()
surface = pygame.display.set_mode((constants.SURFACE_WIDTH ,constants.SURFACE_HEIGHT))
name = pygame.display.set_caption("Djambi")
surface.fill(constants.COLOR_WHITE)

# Title of the game
text_surface = pygame.font.Font(constants.MYFONT, 30).render('Djambi Game', False, constants.COLOR_BLACK)
text_rect = text_surface.get_rect()
text_rect.centerx = surface.get_rect().centerx

# Button
button_play = classes.Button.MiddleButton((200, 50), "Play")
button_quit = classes.Button.MiddleButton((200, 50), "Quit", (0,75))

# Sound
mixer.init()
sound_of_game = mixer.music.load("test.mp3")
mixer.music.set_volume(1)
mixer.music.play()

button_volume_on = classes.Button.VolumeButton((50, 50), "ON")
button_volume_off = classes.Button.VolumeButton((50, 50), "OFF")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or button_quit.is_clicked(event):
            running = False

        if button_volume_on.is_clicked(event):
            mixer.music.set_volume(0)
        
        if button_volume_off.is_clicked(event):
            mixer.music.set_volume(1)

    surface.blit(text_surface, text_rect.topleft)
    button_play.draw(surface)
    button_quit.draw(surface)
    button_volume_on.draw(surface)

    pygame.display.flip()

pygame.quit()
print("fermeture du jeu")