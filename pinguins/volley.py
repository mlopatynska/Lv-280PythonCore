import pygame
import time
import math

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

gameExit = False

display_width = 1000
display_hidht = 800
display = pygame.display.set_mode((display_width, display_hidht))
pygame.display.set_caption("Funny volleyball")
bg = pygame.image.load("beach.jpg")
ball = pygame.image.load("ball.png")
player1 = pygame.image.load("player.png")
player2 = pygame.image.load("player.png")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# player1
x1 = 750
y1 = 600

# player2
x2 = 100
y2 = 600

# ball
x3 = 440
y3 = 200
dx3 = 2
dy3 = 2



# background music
pygame.mixer.music.load("start.wav")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)



font = pygame.font.SysFont('Ravie', 70, True, False)
font2 = pygame.font.SysFont('Ravie', 40, True, False)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, [200, 200])

def message_to_screen2(msg, color):
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, [150, 200])




def game_intro():
    intro = True
    while intro:

        for event in pygame.event.get:
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SLASH:
                    intro = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


        display.fill (BLUE)
        message_to_screen2 ("VOLLEYBALL", RED)
        pygame.display.update()
        clock.tick(30)






while not gameExit:
    #game_intro()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 -= 30
            if event.key == pygame.K_RIGHT:
                x1 += 30
            if event.key == pygame.K_a:
                x2 -= 30
            if event.key == pygame.K_d:
                x2 += 30

        if x1 > 875:
            x1 = 875

        if x1 < 510:
            x1 = 510

        if x2 > 365:
            x2 = 365

        if x2 < 0:
            x2 = 0

    # ball mooving
    x3 += dx3
    y3 += dy3

    if y3 < -40 or y3 > display_hidht - 110:
        dy3 *= -1

    if x3 < -30 or x3 > display_width - 110:
        dx3 *= -1

    #ball vs players
    if x3 > x1-50 and y3 > y1-100:
        dx3 *= -1
        dy3 *= -1

    if x3 < x1 + 50 and y3 > y1-100:
        dx3 *= +1
        dy3 *= -1

    if x3 > x2-50 and y3 > y2-100:
        dx3 *= -1
        dy3 *= -1

    if x3 < x2 + 50 and y3 > y2-100:
        dx3 *= +1
        dy3 *= -1

    if y3 > 680:
        gameExit = True


    # ball vs wall




    display.blit(bg, [0, 0])
    display.blit(player1, [x1, y1])
    display.blit(player2, [x2, y2])
    display.blit(ball, [x3, y3])
    pygame.draw.rect(display, BLACK, [490, 400, 20, 400])
    pygame.display.update()
    clock.tick(90)

message_to_screen("GAME OVER", RED)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()

