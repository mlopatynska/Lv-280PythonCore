import pygame
pygame.init()

screen_x = 1280
screen_y = 720
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption('Bunny running')

done = False

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SKY = (0, 126, 255)
YELLOW = (255,255,0)
circle_x = 30
circle_y = 30
radius = 30

font = pygame.font.SysFont('Calibri', 25, True, False)

image_pos_x = 400
image_pos_y = 300

image_bunny_1 = pygame.image.load("Bunny (1).png")
image_bunny_2 = pygame.image.load("Bunny (2).png")
image_bunny_3 = pygame.image.load("Bunny (3).png")
image_bunny_4 = pygame.image.load("Bunny (4).png")
image_bunny_5 = pygame.image.load("Bunny (5).png")
image_bunny_6 = pygame.image.load("Bunny (6).png")
image_bunny_7 = pygame.image.load("Bunny (7).png")
image_bunny_8 = pygame.image.load("Bunny (8).png")
gif_number = 0
bunny_x = 0
bunny_y = screen_y - 170

jump_or_fall = "jump"

image_carrot = pygame.image.load("cartoon-carrot.png")

click_sound = pygame.mixer.Sound("Ok.wav")

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
        elif event.type == pygame.MOUSEMOTION:
            player_position = pygame.mouse.get_pos()
            image_pos_x = player_position[0]
            image_pos_y = player_position[1]
    # --- Game logic should go here
    # --- Drawing code should go here

    screen.fill(SKY)
    pygame.draw.rect(screen, GREEN, [0, screen_y - 100, screen_x, 200])
    pygame.draw.circle(screen, YELLOW, [screen_x, 0], screen_x/8)

    # if event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_LEFT:
    #         circle_x -= 5
    #     elif event.key == pygame.K_RIGHT:
    #         circle_x += 5
    # if event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_DOWN:
    #         circle_y += 5
    #     if event.key == pygame.K_UP:
    #         circle_y -= 5
    # if event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_1:
    #         radius += 2
    #         if radius >= 400:
    #             radius = 400
    #     if event.key == pygame.K_2:
    #         radius -= 2
    #         if radius <= 0:
    #             radius = 2

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            click_sound.play()

        # Regular bunny
    # if gif_number == 1:
    #     screen.blit(image_bunny_1, [i, 430])
    #     gif_number = 2
    # elif gif_number == 2:
    #     screen.blit(image_bunny_2, [i, 430])
    #     gif_number = 3
    # elif gif_number == 3:
    #     screen.blit(image_bunny_3, [i, 430])
    #     gif_number = 4
    # elif gif_number == 4:
    #     screen.blit(image_bunny_4, [i, 430])
    #     gif_number = 5
    # elif gif_number == 5:
    #     screen.blit(image_bunny_5, [i, 430])
    #     gif_number = 6
    # elif gif_number == 6:
    #     screen.blit(image_bunny_6, [i, 430])
    #     gif_number = 7
    # elif gif_number == 7:
    #     screen.blit(image_bunny_7, [i, 430])
    #     gif_number = 8
    # elif gif_number == 8:
    #     screen.blit(image_bunny_8, [i, 430])
    #     gif_number = 1
    # if i > 800:
    #     i = -200
    # else:
    #     i += 20

        # Slower bunny for 60 fps
    # To make bunny run slower
    slow_coef = 5
    if gif_number in range(0, slow_coef):
        screen.blit(image_bunny_1, [bunny_x, bunny_y])
        gif_number += 1
    elif gif_number in range(slow_coef, slow_coef*2):
        screen.blit(image_bunny_2, [bunny_x, bunny_y])
        gif_number += 1
    elif gif_number in range(slow_coef*2, slow_coef*3):
        screen.blit(image_bunny_3, [bunny_x, bunny_y])
        gif_number += 1
    elif gif_number in range(slow_coef*3, slow_coef*4):
        screen.blit(image_bunny_4, [bunny_x, bunny_y])
        gif_number += 1
    elif gif_number in range(slow_coef*4, slow_coef*5):
        screen.blit(image_bunny_5, [bunny_x, bunny_y])
        gif_number += 1
    elif gif_number in range(slow_coef*5, slow_coef*6):
        screen.blit(image_bunny_6, [bunny_x, bunny_y])
        gif_number += 1
    elif gif_number in range(slow_coef*6, slow_coef*7):
        screen.blit(image_bunny_7, [bunny_x, bunny_y])
        gif_number += 1
    elif gif_number in range(slow_coef*7, slow_coef*8):
        screen.blit(image_bunny_8, [bunny_x, bunny_y])
        gif_number += 1
        if gif_number >= slow_coef*8:
            gif_number = 0

    # Bunny running
    if bunny_x > screen_x:
        bunny_x = -200
    elif gif_number in range(0, 999, slow_coef):
        bunny_x += 40

    # Bunny jumping
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and jump_or_fall == "jump":
            bunny_y -= 10
            if bunny_y <= screen_y/2-170:
                bunny_y = screen_y/2-170
                jump_or_fall = "fall"
        elif jump_or_fall == "fall":
            bunny_y += 10
            if bunny_y >= screen_y - 170:
                bunny_y = screen_y - 170
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            bunny_y += 10
            jump_or_fall = "fall"
            if bunny_y >= screen_y - 170:
                bunny_y = screen_y - 170
                jump_or_fall = "jump"


    for carrot_pos in range(screen_x/2, screen_x*2/3, 50):
        screen.blit(image_carrot, [carrot_pos, screen_y/2])

    screen.blit(image_carrot, [image_pos_x, image_pos_y])

    text = font.render("Bunny running", True, YELLOW)
    screen.blit(text, [screen_x/2-50, 10])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
quit()