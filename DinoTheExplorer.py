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

jumping = False

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

font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)

score = 0
passed = False

start = 0
playing = 1
paused = 2 
over = 3

state = start

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and state == start:
                    state = playing
                    dino_speed = jump
                    jumping = True

            elif event.key == pygame.K_SPACE and state == playing:
                if dino_y + dino_height >= ground:
                    dino_speed = jump
                    jumping = True

            elif event.key == pygame.K_RETURN and state == over:

                state = playing

                dino_y = ground - dino_height
                dino_speed = 0

                obstacle_x = 800
                obstacle_width = 25

                score = 0
                passed = False

                jumping = False

            elif event.key == pygame.K_ESCAPE and state == playing:
                    state = paused

            elif event.key == pygame.K_ESCAPE and state == paused:
                    state = playing

        if event.type == pygame.KEYUP:
             if event.key == pygame.K_SPACE:
                  jumping = False

    if state == playing:

        if jumping == True and dino_speed < 0:
             dino_speed = dino_speed - 0.35

        dino_speed = dino_speed + gravity

        dino_y = dino_y + dino_speed

        if dino_y + dino_height >= ground:
            dino_y = ground - dino_height
            dino_speed = 0
            jumping = False

        obstacle_x = obstacle_x - obstacle_speed

        if obstacle_x + obstacle_width < dino_x and passed == False:
            score = score + 1
            passed = True

        if obstacle_x + obstacle_width < 0:
            obstacle_x = random.randint(800, 1100)

            obstacle_type = random.randint(1,2)

            if obstacle_type == 1:
                 obstacle_width = 25

            else:
                 obstacle_width = 55

            passed = False

        if dino_x + dino_width > obstacle_x:

            if dino_x < obstacle_x + obstacle_width:

                if dino_y + dino_height > ground - obstacle_height:
                    state = over

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

    score_text = small_font.render(
        "score: " + str(score),
        True,
        (0, 0, 0)
    )

    screen.blit(
        score_text,
        (650,20)
    )

    if state == start:

        start_text = font.render(
            "PRESS SPACE",
            True,
            (0, 0, 0)
        )

        screen.blit(
            start_text,
            (240, 100)
        )

    if state == over:

        over_text = font.render(
            "GAME OVER",
            True,
            (0, 0, 0)
        )

        restart_text = small_font.render(
            "Press ENTER to RESTART",
            True,
            (0, 0, 0)
        )

        screen.blit(
            over_text,
            (270, 100)
        )

        screen.blit(
            restart_text,
            (250, 170)
        )

    if state == paused:

        pause_text = font.render(
            "PAUSED",
            True,
            (0, 0, 0)
        )

        resume_text = small_font.render(
            "Pess ESC to Resume",
            True,
            (0, 0, 0)
        )

        screen.blit(
            pause_text,
            (300,100)
        )

        screen.blit(
            resume_text,
            (270, 170)
        )

    pygame.display.flip()

    clock.tick_busy_loop(60)
    
pygame.quit()