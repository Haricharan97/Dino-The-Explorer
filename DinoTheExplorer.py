import pygame

pygame.init()

width = 800
height = 400

scren = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    scren.fill((240,240,240))

    pygame.display.update()

    clock.tick(60)
    
pygame.quit()