import random
import pygame

pygame.init()
win = pygame.display.set_mode((1000, 500))
bg_img = pygame.image.load("road.png")
bg = pygame.transform.scale(bg_img, (1000, 500))

width = 1000
height = 500
i = 0



run = True
while run:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    win.fill((0,0,0))

    #Create looping background
    win.blit(bg, (0, i))
    win.blit(bg, (0, i-height))
    if i == +height:
        win.blit(bg, (0, i+height))
        i = 0
    i += 4


    pygame.display.update()
