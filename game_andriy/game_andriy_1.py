import pygame
import random
pygame.init()

screen_x = 1280
screen_y = 720
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption('Bunny running v3.0 beta')

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
DARKER_GREEN = (0,200,0)
BLUE = (0,0,255)
SKY = (0, 126, 255)
YELLOW = (255,255,0)
ORANGE = (255, 126, 0)

font = pygame.font.SysFont('Calibri', 25, True, False)
font_large = pygame.font.SysFont('Calibri', 72, True, False)


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

image_bunny_1_rect = image_bunny_1.get_rect()
image_bunny_2_rect = image_bunny_2.get_rect()
image_bunny_3_rect = image_bunny_3.get_rect()
image_bunny_4_rect = image_bunny_4.get_rect()
image_bunny_5_rect = image_bunny_5.get_rect()
image_bunny_6_rect = image_bunny_6.get_rect()
image_bunny_7_rect = image_bunny_7.get_rect()
image_bunny_8_rect = image_bunny_8.get_rect()

image_bunny_all_rect = image_bunny_1_rect.unionall([image_bunny_2_rect, image_bunny_3_rect,
                                            image_bunny_4_rect, image_bunny_5_rect, image_bunny_6_rect,
                                            image_bunny_7_rect, image_bunny_8_rect])

image_bunny_all_rect[1] = screen_y - 170

background_image = pygame.transform.scale(pygame.image.load("the-house-in-the-field.jpg"), (screen_x, screen_y))

gif_number = 0
bunny_x = 0
bunny_y = screen_y - 170

jump_or_fall = "jump"

image_carrot = pygame.image.load("cartoon-carrot.png")
image_carrot_rect = image_carrot.get_rect()
# carrot_positions = {}
#
# for carrot_pos in range(screen_x / 2, screen_x * 2 / 3, 50):
#     carrot_positions[(carrot_pos, screen_y / 2)] = 1
carrot_positions = []

for carrot_pos in range(screen_x / 6, screen_x*20, 120):
    carrot_positions.append([carrot_pos, random.randint(screen_y / 2, (screen_y / 2 + screen_y - 170)) / 2])
    carrot_positions.append([carrot_pos, random.randint((screen_y / 2 + screen_y - 170) / 2, screen_y - 170)])

score = 0
score_full = 50
click_sound = pygame.mixer.Sound("Ok.wav")
time = []
speed = 40

# -------- Main Program Loop -----------
while True:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
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

    # screen.fill(SKY)
    # pygame.draw.rect(screen, GREEN, [0, screen_y - 100, screen_x, 200])
    # pygame.draw.circle(screen, YELLOW, [screen_x, 0], screen_x / 8)

    screen.blit(background_image, (0, 0))

    # for i in range(len(carrot_positions)):
    #     image_carrot_rect[0], image_carrot_rect[1] = carrot_positions.keys()[i][0], carrot_positions.keys()[i][1]
    #     screen.blit(image_carrot, carrot_positions.keys()[i])
    #     if image_bunny_all_rect.colliderect(image_carrot_rect):
    #         pass

    for i in carrot_positions:
        screen.blit(image_carrot, i)
        if pygame.Rect(image_bunny_all_rect[0]+image_bunny_all_rect[2]*3/4, image_bunny_all_rect[1], image_bunny_all_rect[2]/8,
            image_bunny_all_rect[3]).colliderect(i, [image_carrot_rect[2], image_carrot_rect[3]]):
            carrot_positions.remove(i)
            score += 1

    screen.blit(pygame.transform.rotate(image_carrot, -135), [image_pos_x, image_pos_y])

    text = font.render("Bunny running", True, YELLOW)
    screen.blit(text, [screen_x/2-50, 10])

    score_text = font.render("Score: {}".format(score), True, WHITE)
    screen.blit(score_text, [0, 0])

    hunger_text = font.render("HUNGER:", True, WHITE)
    screen.blit(hunger_text, [0, 29])

    if score < score_full*0.25:
        progress_color = RED
    elif score < score_full*0.5:
        progress_color = ORANGE
    elif score < score_full*0.75:
        progress_color = YELLOW
    elif score <= score_full:
        progress_color = GREEN

    if score >= score_full:
        time.append(float(pygame.time.get_ticks()) / 1000)
        time_text = font_large.render("Your time is {0:.2f} sec".format(time[0]), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect[0], time_rect[1] = screen_x / 2 - time_rect[2] / 2, screen_y / 2 - time_rect[3] / 2
        screen.blit(time_text, time_rect)
        screen.blit(image_bunny_8, image_bunny_all_rect)
        jump_or_fall = "fall"
        gif_number = 997
        if image_bunny_all_rect[1] < screen_y - 170:
            image_bunny_all_rect[0] += int(speed/slow_coef)

        continue_text = font_large.render("Continue", True, WHITE)
        continue_rect = continue_text.get_rect()
        continue_rect[0], continue_rect[1] = screen_x / 2 - continue_rect[2] / 2, time_rect.bottom
        pygame.draw.rect(screen, DARKER_GREEN, continue_rect)
        screen.blit(continue_text, continue_rect)

    pygame.draw.rect(screen, progress_color, [100, 30, 200*float(score_full - score)/float(score_full) if score < score_full else 1, 20])

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

    #     Slower bunny for 60 fps
    # To make bunny run slower
    slow_coef = 5
    if gif_number in range(0, slow_coef):
        screen.blit(image_bunny_1, image_bunny_all_rect)
        gif_number += 1
    elif gif_number in range(slow_coef, slow_coef*2):
        screen.blit(image_bunny_2, image_bunny_all_rect)
        gif_number += 1
    elif gif_number in range(slow_coef*2, slow_coef*3):
        screen.blit(image_bunny_3, image_bunny_all_rect)
        gif_number += 1
    elif gif_number in range(slow_coef*3, slow_coef*4):
        screen.blit(image_bunny_4, image_bunny_all_rect)
        gif_number += 1
    elif gif_number in range(slow_coef*4, slow_coef*5):
        screen.blit(image_bunny_5, image_bunny_all_rect)
        gif_number += 1
    elif gif_number in range(slow_coef*5, slow_coef*6):
        screen.blit(image_bunny_6, image_bunny_all_rect)
        gif_number += 1
    elif gif_number in range(slow_coef*6, slow_coef*7):
        screen.blit(image_bunny_7, image_bunny_all_rect)
        gif_number += 1
    elif gif_number in range(slow_coef*7, slow_coef*8):
        screen.blit(image_bunny_8, image_bunny_all_rect)
        gif_number += 1
        if gif_number in range(slow_coef*8, slow_coef*9+1):
            gif_number = 0


    # Bunny constantly running
    if image_bunny_all_rect[0] > screen_x:
        image_bunny_all_rect[0] = -200
        for carrot_pos in carrot_positions:
            carrot_pos[0] -= screen_x +100
    elif gif_number in range(0, 1000, slow_coef):
        image_bunny_all_rect[0] += speed

    # Bunny jumping
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and jump_or_fall == "jump":
            image_bunny_all_rect[1] -= 20
            if image_bunny_all_rect[1] <= screen_y/2-170:
                image_bunny_all_rect[1] = screen_y/2-170
                jump_or_fall = "fall"
        elif jump_or_fall == "fall":
            image_bunny_all_rect[1] += 10
            if image_bunny_all_rect[1] >= screen_y - 170:
                image_bunny_all_rect[1] = screen_y - 170
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            image_bunny_all_rect[1] += 10
            jump_or_fall = "fall"
            if image_bunny_all_rect[1] >= screen_y - 170:
                image_bunny_all_rect[1] = screen_y - 170
                jump_or_fall = "jump"

    if image_bunny_all_rect.colliderect(image_carrot_rect):
        print "It works!"

    # print image_carrot_rect

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
quit()