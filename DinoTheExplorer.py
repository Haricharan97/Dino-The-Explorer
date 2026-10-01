import pygame
import random

pygame.init()

width = 800
height = 400

dino_x = 100
dino_y = 280

dino_width = 40
dino_height = 70

normal_height = 70
crouch_height = 35

dino_speed = 0
gravity = 0.8
jump = -12

current_jump = jump

jumping = False

fast_fall = 1.2

screen = pygame.display.set_mode(
    (width, height),
    pygame.DOUBLEBUF,
    vsync= 1
    )

pygame.display.set_caption("Dino The Explorer")

clock = pygame.time.Clock()

ground = 350
obstacle_speed = 5
high_obstacle = 280
low_obstacle = 320

level = 1 

gap_min = 400
gap_max = 550

obstacles = [
    [800, 1, 25, 70, False],
    [1150, 2, 55, 70, False]
]

coin_x = 1000
coin_y = 300

coin_size = 20

coins = 0

coin_type = 1

clouds = [
    [100, 70, 1.0],
    [350, 110, 0.7],
    [650, 50, 1.2]
]

cloud_speed = 1

font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)

score = 0
high_score = 0

lives = 3

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

            elif event.key == pygame.K_UP and state == playing:
                if dino_y + dino_height >= ground:
                    dino_height = normal_height
                    dino_y = ground - dino_height
                    current_jump = jump
                    dino_speed = current_jump
                    jumping = True

            elif event.key == pygame.K_SPACE and state == over:

                state = playing

                dino_height = normal_height
                dino_y = ground - dino_height
                dino_speed = 0

                score = 0
                jumping = False

                level = 1 
                obstacle_speed = 5

                gap_min = 400
                gap_max = 550

                obstacles = [
                    [800, 1, 25, 70, False],
                    [1150, 2, 55, 70, False]
                ]

                coins = 0

                coin_x = 1000
                coin_y = 300
                coin_type = 1

                lives = 3

            elif event.key == pygame.K_ESCAPE and state == playing:
                state = paused

            elif event.key == pygame.K_SPACE and state == paused:
                state = playing

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                  jumping = False

                  if dino_speed < -5:
                      dino_speed = -5

    if state == playing:

        hit = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] and dino_y + dino_height >= ground:
             
            dino_height = crouch_height
            dino_y = ground - dino_height

        else:

            if dino_y + dino_height >= ground:
                  
                dino_height = normal_height
                dino_y = ground - dino_height

        if jumping == True and dino_speed < 0:
            dino_speed = dino_speed - 0.25

        dino_speed = dino_speed + gravity

        if keys[pygame.K_DOWN] and dino_y + dino_height < ground:
            dino_speed = dino_speed + fast_fall

        dino_y = dino_y + dino_speed

        if dino_y + dino_height >= ground:
            dino_y = ground - dino_height
            dino_speed = 0
            jumping = False

        if score < 5:

            level = 1

            obstacle_speed = 5

            gap_min = 400
            gap_max = 550

        elif score < 10:

            level = 2

            obstacle_speed = 6

            gap_min = 350
            gap_max = 500

        elif score < 20:

            level = 3

            obstacle_speed = 7

            gap_min = 300
            gap_max = 450

        else:

            level = 4

            obstacle_speed = 8

            gap_min = 300
            gap_max = 400

        for cloud in clouds:
                    cloud[0] = cloud[0] - cloud_speed
                    if cloud[0] < - 100:
                        cloud[0] = width + random.randint(100, 300)
                        cloud[1] = random.randint(40, 150)
                        cloud[2] = random.choice([0.7, 1.0, 1.2])

        for obstacle in obstacles:

            obstacle[0] = obstacle[0] - obstacle_speed

            if obstacle[0] + obstacle[2] < dino_x and obstacle[4] == False:

                score = score + 1
                obstacle[4] = True

                if score > high_score:
                    high_score = score

            if obstacle[0] + obstacle[2] < 0:

                if obstacles[0][0] > obstacles[1][0]:

                    furtest_x = obstacles[0][0]
                    furthest_width = obstacles[0][2]
                    previous_type = obstacles[0][1]

                else:
                    furtest_x = obstacles[1][0]
                    furthest_width = obstacles[1][2]
                    previous_type = obstacles[1][1]


                if level == 1:
                    obstacle[1] = random.randint(1,2)

                elif level == 2:
                    obstacle[1] = random.randint(1,3)

                else:
                    obstacle[1] = random.randint(1,5)

                if obstacle[1] == 1:

                    obstacle[2] = random.randint(20, 30)
                    obstacle[3] = random.randint(55, 75)

                elif obstacle[1] == 2:

                    obstacle[2] = random.randint(45, 65)
                    obstacle[3] = random.randint(60, 85)

                elif obstacle[1] == 3:

                    obstacle[2] = 50
                    obstacle[3] = 25

                elif obstacle[1] == 4:

                    obstacle[2] = 50
                    obstacle[3] = 25

                elif obstacle[1] == 5:

                    obstacle[2] = random.randint(90, 140)
                    obstacle[3] = random.randint(35, 50)

                gap = random.randint(
                    gap_min,
                    gap_max
                )

                gap = gap + int(
                    (obstacle_speed -5) * 25
                )

                if obstacle[1] == 2:
                    gap = gap + 30

                if previous_type == 3 or previous_type == 4:

                    if obstacle[1] == 3 or obstacle[1] == 4:

                        gap = gap + 70

                obstacle[0] = max(
                    width,
                    furtest_x + furthest_width + gap
                )

                if obstacle[0] + obstacle[2] > coin_x - 100:
                    if obstacle[0] < coin_x + coin_size + 100:

                        obstacle[0]= (coin_x + coin_size + 150)

                obstacle[4] = False

            if obstacle[1] == 1 or obstacle[1] == 2:

                if dino_x + dino_width > obstacle[0]:

                    if dino_x < obstacle[0] + obstacle[2]:

                        if dino_y + dino_height > ground - obstacle[3]:
                            hit = True

            elif obstacle[1] == 3:

                if dino_x + dino_width > obstacle[0]:

                    if dino_x < obstacle[0] + obstacle[2]:

                        if dino_y < high_obstacle + obstacle[3]:

                            if dino_y + dino_height > high_obstacle:
                                hit = True

            elif obstacle[1] == 4:

                if dino_x + dino_width > obstacle[0]:

                    if dino_x < obstacle[0] + obstacle[2]:

                        if dino_y < low_obstacle + obstacle[3]:

                            if dino_y + dino_height > low_obstacle:

                                hit = True

            elif obstacle[1] == 5:
                if dino_x + dino_width > obstacle[0]:
                    if dino_x < obstacle[0] + obstacle[2]:
                        if dino_y + dino_height > ground - obstacle[3]:
                            hit = True

        if hit == True:

            lives = lives - 1

            if lives == 0:
                state = over

            else:

                dino_height = normal_height
                dino_y = ground - dino_height
                dino_speed = 0
                jumping = False

                obstacles[0][0] = 800
                obstacles[1][0] = 1200

                obstacles[0][4] = False
                obstacles[1][4] = False

        coin_x = coin_x - obstacle_speed

        if dino_x + dino_width > coin_x:

            if dino_x < coin_x + coin_size:

                if dino_y + dino_height > coin_y:

                    if dino_y < coin_y + coin_size:

                        if coin_type == 1:
                            coins = coins + 1

                        elif coin_type == 2:
                            coins = coins + 5

                        coin_x = width + random.randint(300, 600)

                        for obstacle in obstacles:

                            if coin_x + coin_size > obstacle[0] - 100:

                                if coin_x < obstacle[0] + obstacle[2] + 100:

                                    coin_x = (obstacle[0] + obstacle[2] + 150)

                        coin_y = random.choice(
                            [220, 260, 300]
                        )

                        coin_chance = random.randint(1, 5)

                        if coin_chance == 1:
                            coin_type = 2

                        else:
                            coin_type = 1

        if coin_x + coin_size < 0:

            coin_x = width + random.randint(300, 600)

            for obstacle in obstacles:

                if coin_x + coin_size > obstacle[0] - 100:

                    if coin_x < obstacle[0] + obstacle[2] + 100:

                        coin_x = (obstacle[0] + obstacle[2] + 150)

            coin_y = random.choice(
                [220, 260, 300]
            )

            coin_chance = random.randint(1, 5)

            if coin_chance == 1:
                coin_type = 2

            else:
                coin_type = 1

    screen.fill((135, 206, 240))

    for cloud in clouds:

        cloud_x = int(cloud[0])
        cloud_y = int(cloud[1])
        cloud_size = cloud[2]

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (
                cloud_x,
                cloud_y
            ),
            int(18 * cloud_size)
        )

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (
                cloud_x + int(20 * cloud_size),
                cloud_y - int(8 * cloud_size)
            ),
            int(22 * cloud_size),
        )

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (
                cloud_x + int(42 * cloud_size),
                cloud_y
            ),
            int(18 * cloud_size)
        )

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (
                cloud_x,
                cloud_y,
                int(45 * cloud_size),
                int(18 * cloud_size)
            )
        )

    pygame.draw.rect(
        screen,
        (150, 95, 55),
        (0, ground, width, height - ground),
    )

    pygame.draw.rect(
        screen,
        (120, 75, 45),
        (0, ground + 25, width, height - ground - 25)
    )

    pygame.draw.rect(
        screen,
        (70, 170, 70),
        (0, ground - 8, width, 12)
    )

    pygame.draw.rect(
        screen,
        (110, 200, 90),
        (0, ground - 8, width, 4)
    )

    pygame.draw.rect(
        screen,
        (60, 150, 70),
        (
            int(dino_x),
            int(dino_y + 20), 
            28, 
            dino_height - 20
        )
    )

    pygame.draw.rect(
        screen,
        (60, 150, 70),
        (
            int(dino_x + 20),
            int(dino_y),
            20,
            25
        )
    )

    pygame.draw.rect(
        screen,
        (60, 150, 70),
        (
            int(dino_x + 32),
            int(dino_y + 10),
            14,
            10
        )
    )

    pygame.draw.rect(
        screen,
        (60, 150, 70),
        (
            int(dino_x - 12),
            int(dino_y + 32),
            15,
            10
        )
    )

    pygame.draw.rect(
        screen,
        (45, 120, 55),
        (
            int(dino_x + 4),
            int(dino_y + dino_height - 16),
            8,
            16
        )
    )

    pygame.draw.rect(
        screen,
        (45, 120, 55),
        (
            int(dino_x + 20),
            int(dino_y + dino_height - 15),
            8,
            16
        )
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (
            int(dino_x + 28),
            int(dino_y + 5),
            6,
            6
        )
    )

    for obstacle in obstacles:

        obstacle_x = int(obstacle[0])
        obstacle_width = obstacle[2]
        obstacle_height = obstacle[3]

        if obstacle[1] == 1:

            cactus_y = ground - obstacle_height

            pygame.draw.rect(
                screen,
                (30, 130, 55),
                (
                    obstacle_x,
                    cactus_y,
                    obstacle_width,
                    obstacle_height
                )
            )

            pygame.draw.rect(
                screen,
                (55, 165, 70),
                (
                    obstacle_x + 4,
                    cactus_y + 5,
                    4,
                    obstacle_height - 10
                )
            )

            pygame.draw.rect(
                screen,
                (30, 130, 55),
                (
                    obstacle_x - 7,
                    cactus_y + 25,
                    9,
                    8 
                )
            )

            pygame.draw.rect(
                screen,
                (30, 130, 55),
                (
                    obstacle_x - 7,
                    cactus_y + 17,
                    6,
                    15
                )
            )

            pygame.draw.rect(
                screen,
                (30, 130, 55),
                (
                    obstacle_x + obstacle_width - 2,
                    cactus_y + 35,
                    8,
                    8
                )
            )

            pygame.draw.rect(
                screen,
                (30, 130, 55),
                (
                    obstacle_x + obstacle_width + 2,
                    cactus_y + 27,
                    5,
                    15
                )
            )

        elif obstacle[1] == 2:
            cactus_y = ground - obstacle_height
            pygame.draw.rect(
                screen,
                (25, 115, 50),
                (
                    obstacle_x,
                    cactus_y,
                    obstacle_width,
                    obstacle_height
                )
            )

            pygame.draw.rect(
                screen,
                (55, 155, 65),
                (
                    obstacle_x + obstacle_width // 2 - 3,
                    cactus_y + 4,
                    6,
                    obstacle_height - 8
                )
            )

            pygame.draw.rect(
                screen,
                (25, 115, 50),
                (
                    obstacle_x - 10,
                    cactus_y + 30,
                    12,
                    10
                )
            )

            pygame.draw.rect(
                screen,
                (25, 115, 50),
                (
                    obstacle_x - 10,
                    cactus_y + 18,
                    7,
                    20
                )
            )

            pygame.draw.rect(
                screen,
                (25, 115, 50),
                (
                    obstacle_x + obstacle_width - 2,
                    cactus_y + 20,
                    12,
                    10
                )
            )

            pygame.draw.rect(
                screen,
                (25, 115, 50),
                (
                    obstacle_x + obstacle_width + 4,
                    cactus_y + 10,
                    6,
                    20
                )
            )

        elif obstacle[1] == 3: 
            bird_y = high_obstacle

            pygame.draw.rect(
                screen,
                (180, 50, 50),
                (
                    obstacle_x,
                    bird_y,
                    obstacle_width,
                    obstacle_height
                )
            )

            pygame.draw.rect(
                screen,
                (120, 30, 30),
                (
                    obstacle_x + 20,
                    bird_y + 7,
                    20,
                    10
                )
            )

            pygame.draw.rect(
                screen,
                (230, 160, 40),
                [
                    obstacle_x - 18,
                    bird_y + 10,
                    18,
                    6
                ]
            )

            pygame.draw.circle(
                screen,
                (255, 255, 255),
                (
                    obstacle_x + 8,
                    bird_y + 7   
                ),
                4
            )

            pygame.draw.circle(
                screen,
                (0, 0, 0),
                (
                    obstacle_x + 6,
                    bird_y + 7
                ),
                2
            )

        elif obstacle[1] == 4:
        
                bird_y = low_obstacle

                pygame.draw.rect(
                    screen,
                    (180, 50, 50),
                    (
                        obstacle_x,
                        bird_y,
                        obstacle_width,
                        obstacle_height
                    )
                )

                pygame.draw.rect(
                    screen,
                    (230, 160, 40),
                    (
                        obstacle_x - 18,
                        bird_y + 7,
                        20, 
                        10
                    )
                )

                pygame.draw.rect(
                    screen,
                    (230, 160, 40),
                    (
                        obstacle_x - 18,
                        bird_y + 10,
                        18,
                        6
                    )
                )

                pygame.draw.circle(
                    screen,
                    (255, 255, 255),
                    (
                        obstacle_x + 8,
                        bird_y + 7
                    ),
                    4
                )

                pygame.draw.circle(
                    screen,
                    (0, 0, 0),
                    (
                        obstacle_x + 6,
                        bird_y + 7
                    ),
                    2
                )

        elif obstacle[1] == 5:
            pygame.draw.rect(
                screen,
                (20, 150, 50),
                (
                    int(obstacle[0]),
                    ground - obstacle[3],
                    obstacle[2],
                    obstacle[3]
                )
            )

    if coin_type == 1:

        coin_cx = int(coin_x) + coin_size // 2
        coin_cy = int(coin_y) + coin_size // 2

        pygame.draw.circle(
            screen,
            (180, 120, 0),
            (coin_cx, coin_cy),
            coin_size // 2
        )

        pygame.draw.circle(
            screen,
            (255, 190, 0),
            (coin_cx, coin_cy),
            coin_size // 2 - 2 
        )

        pygame.draw.circle(
            screen,
            (255, 225, 80),
            (coin_cx, coin_cy),
            coin_size // 2 - 5
        )

        pygame.draw.circle(
            screen,
            (255, 245, 100),
            (coin_cx - 3, coin_cy - 3),
            2
        )

    elif coin_type == 2:

        coin_cx = int(coin_x) + coin_size // 2
        coin_cy = int(coin_y) + coin_size // 2
        
        pygame.draw.circle(
            screen,
            (255, 245, 120),
            (coin_cx, coin_cy),
            coin_size // 2 + 5
        )

        pygame.draw.circle(
            screen,
            (190, 90, 0),
            (coin_cx, coin_cy),
            coin_size // 2 + 2
        )

        pygame.draw.circle(
            screen,
            (255, 210, 0),
            (coin_cx, coin_cy),
            coin_size // 2
        )

        pygame.draw.circle(
            screen,
            (255, 140, 0),
            (coin_cx, coin_cy),
            coin_size // 2 - 3
        )

        star_points = [
            (coin_cx, coin_cy - 6),
            (coin_cx + 2, coin_cy - 2),
            (coin_cx + 6, coin_cy - 2),
            (coin_cx + 3, coin_cy + 1),
            (coin_cx + 4, coin_cy + 6),
            (coin_cx, coin_cy + 3),
            (coin_cx - 4, coin_cy + 6),
            (coin_cx - 3, coin_cy + 1),
            (coin_cx - 6, coin_cy - 2),
            (coin_cx - 2, coin_cy - 2)
        ]

        pygame.draw.polygon(
            screen,
            (255, 255, 180),
            star_points
        )

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (coin_cx - 4, coin_cy - 5),
            2
        )

    score_text = small_font.render(
        "Score: " + str(score),
        True,
        (0, 0, 0)
    )

    screen.blit(
        score_text,
        (650,20)
    )

    high_score_text = small_font.render(
         "High: " + str(high_score),
         True,
         (0, 0, 0)
    )

    screen.blit(
         high_score_text,
         (20, 20)
    )

    coin_text = small_font.render(
        "Coins: " + str(coins),
        True,
        (0, 0, 0)
    )

    screen.blit(
        coin_text,
        (650,50)
    )

    lives_text = small_font.render(
        "lives: " + str(lives),
        True,
        (0, 0, 0)
    )

    screen.blit(
        lives_text,
        (20, 50)
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
            "Press SPACE to RESTART",
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
            "Press SPACE to Resume",
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