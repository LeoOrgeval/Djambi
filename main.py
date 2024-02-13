import pygame
import classes.Button
import constants

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
button_quit = classes.Button.MiddleButton( (200, 50), "Quit", (0,75))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
    
    surface.blit(text_surface, text_rect.topleft)
    # pygame.draw.rect(surface, (0, 0, 255), rect, width=2)
    # surface.blit(text_jouer, text_rect_jouer.topleft)
    button_play.draw(surface)
    button_quit.draw(surface)

    
    pygame.display.flip()