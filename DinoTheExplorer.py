import pygame

pygame.init()

width = 800
height = 400

dino_x = 100
dino_y = 280

dino_height = 70

dino_speed = 0
gravity = 0.8
jump = -15

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

ground = 350

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                if dino_y + dino_height >= ground:
                    dino_speed = jump

    dino_speed = dino_speed + gravity

    dino_y = dino_y + dino_speed

    if dino_y + dino_height >= ground:
        dino_y = ground - dino_height
        dino_speed = 0

    screen.fill((240,240,240))

    pygame.draw.rect(
        screen,
        (180, 180, 180),
        (0, ground, width, height - ground)
    )

    pygame.draw.line(
        screen,
        (0, 0, 0),
        (0, ground),
        (width, ground),
        3
    )

    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (dino_x, dino_y, dino_width, dino_height)
    )

    pygame.display.update()

    clock.tick(60)
    
pygame.quit()