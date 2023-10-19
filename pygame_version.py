class Player:

    def __init__(self, nom, x,y, numero, couleur, poste="ATT", note=50):
        self.nom = nom
        self.x = x
        self.y = y
        self.numero = numero
        self.couleur = couleur
        self.poste = poste
        self.note = note
        self.image = pygame.image.load(f"images/{couleur}_{numero}.svg")

    def draw(self):
        rect = self.image.get_rect()
        rect.centerx = self.x
        rect.centery = self.y
        fenetre.blit(self.image, rect)

import pygame

pygame.init()

fenetre = pygame.display.set_mode((612, 408))
terrain = pygame.image.load('images/terrain.png')
joueur = Player("test", 50, 50, 10, "blue")

while True:
    fenetre.blit(terrain, (0, 0))
    joueur.draw()
    pygame.display.flip()