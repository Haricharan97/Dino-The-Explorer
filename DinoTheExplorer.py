import pygame
import random

pygame.init()

width = 800
height = 400

dino_x = 100
dino_y = 280

dino_width = 40
dino_height = 70

dino_speed = 0
gravity = 0.8
jump = -15

screen = pygame.display.set_mode(
    (width, height),
    pygame.DOUBLEBUF,
    vsync= 1
    )

clock = pygame.time.Clock()

ground = 350

obstacle_x = 800
obstacle_width = 25
obstacle_height = 70
obstacle_speed = 5

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

    obstacle_x = obstacle_x - obstacle_speed

    if obstacle_x + obstacle_width < 0:
        obstacle_x = random.randint(800, 1100)

    screen.fill((240,240,240))

    pygame.draw.rect(
        screen,
        (180, 180, 180),
        (0, ground, width, height - ground)
    )

    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (
            int(dino_x),
            int(dino_y), 
            dino_width, 
            dino_height
            )
    )

    pygame.draw.rect(
        screen,
        (0, 120, 0),
        (
            int(obstacle_x),
            ground - obstacle_height,
            obstacle_width,
            obstacle_height
        )
    )

    pygame.draw.line(
        screen,
        (0, 0, 0),
        (0, ground),
        (width, ground),
        3
    )

    pygame.display.flip()

    clock.tick_busy_loop(60)
    
pygame.quit()