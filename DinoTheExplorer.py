import pygame

pygame.init()

width = 800
height = 400

d_x = 100
d_y = 280

d_width = 40
d_height = 70

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((240,240,240))

    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (d_x, d_y, d_width, d_height)
    )

    pygame.display.update()

    clock.tick(60)
    
pygame.quit()