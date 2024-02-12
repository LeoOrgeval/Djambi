import pygame
# pygame setup
pygame.init()

#generer la fenetre du jeu
screen = pygame.display.set_caption("Djambi")
#clock = pygame.time.Clock()
pygame.display.set_mode((500,500))

#screen.fill("white")

#variable pour dire si la fenetre est ouverte ou non
running = True

#boucle tant que running est vrai
while running:

    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        #si l'evenement est 'la fermeture de la fenetre'
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")


