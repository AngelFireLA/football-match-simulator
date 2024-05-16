import os
import cairosvg
import main
def convert_svg_to_png(svg_file, png_file):
    cairosvg.svg2png(url=svg_file, write_to=png_file)

scale_factor = 0.2

class Player:

    def __init__(self, nom, x, y, numero, couleur, poste="ATT", note=50):
        self.nom = nom
        self.x = x
        self.y = y
        self.numero = numero
        self.couleur = couleur
        self.poste = poste
        self.note = note

        # Define file paths
        svg_file = f"images/{couleur}_{numero}.svg"
        png_file = f"images/{couleur}_{numero}.png"

        # Convert SVG to PNG if PNG does not exist
        if not os.path.exists(png_file):
            convert_svg_to_png(svg_file, png_file)

        # Load the PNG image
        self.image = pygame.image.load(png_file)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*scale_factor, self.image.get_height()*scale_factor))


    def draw(self):
        rect = self.image.get_rect()
        rect.centerx = self.x
        rect.centery = self.y
        fenetre.blit(self.image, rect)

import pygame

pygame.init()

fenetre = pygame.display.set_mode((612, 408))
terrain = pygame.image.load('images/terrain.png')
joueurs = [Player("test", 50*i, 50, i, "blue") for i in range(1, 12)]+[Player("test", 50*i, 200, i, "red") for i in range(1, 12)]
joueur = Player("test", 50, 50, 10, "blue")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:  # Right mouse button clicked
                print("Right mouse button clicked at:", event.pos)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                match = main.Match()
                a, b = match.play_full_match(log=True)
                print(b)
    fenetre.blit(terrain, (0, 0))
    # for j in joueurs:
    #     j.draw()
    pygame.display.flip()