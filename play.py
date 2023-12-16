
import pygame 
import os 
import random 

pygame.font.init()

width, height = 1024, 750

prota = pygame.image.load(os.path.join("nave.png"))
enemigo1 = pygame.image.load(os.path.join("alien.png"))
enemigo2 = pygame.image.load(os.path.join("alien.png"))
enemigo3 = pygame.image.load(os.path.join("alien.png"))
enemigo4 = pygame.image.load(os.path.join("alien.png"))
enemigo5 = pygame.image.load(os.path.join("alien.png"))

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("proyecto tirador")







def main_menu():
    title_font = pygame.font.SysFont("helvetica", 70)
    run = True
    title_label = title_font.render("presiona click para iniciar...", 3, (158, 54, 187))
    title_pos = (width/2 - title_label.get_width()/2, 350)

    while run:
        window.fill((0, 0, 0))
        window.blit(title_label, title_pos)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or x:
                run = False

    pygame.quit()

main_menu()