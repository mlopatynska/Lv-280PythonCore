import pygame
import random
import pygame.mixer
import sys

pygame.init()
pygame.mixer.init()



pygame.mixer.music.load("endofline.ogg")
pygame.mixer.music.play()


white = (255, 255, 255)
black = (0, 0, 0)

display__size = 1024, 609
display = pygame.display.set_mode((display__size))
pygame.display.set_caption("Pin-Pong")

rallyText = pygame.font.SysFont("Times New Roman", 44)
rally = 0
rallyRender = rallyText.render(str(rally), 1, white)



paddle1 = pygame.image.load("Images/paddle.png")
paddle2 = pygame.image.load("Images/paddle.png")
ball = pygame.image.load("Images/ball.png")
bg = pygame.image.load("Images/bg.png")

running = True

player1 = 0
player2 = 0

x1 = 10
y1 = 260

x2 = 1000
y2 = 260
ball_pos = pygame.math.Vector2(385, 285)
ball_speed =pygame.math.Vector2(random.randint(-10, 11), random.randint(-10, 11))
ball_radius = 10

paddle_speed = 40
paddle1_up = False
paddle1_down = False
paddle2_up = False
paddle2_down = False



clock = pygame.time.Clock()

while running:
    
    clock.tick(60)
    ball_pos+=ball_speed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                player1 = 0
                player2 = 0
                ball_speed =(10)
                ball_pos = (385,285)
            if event.key == pygame.K_f:
                ball_speed = (ball_speed * 2)
            if event.key == pygame.K_w:
                paddle1_up = True
            if event.key == pygame.K_s:
                paddle1_down = True
            if event.key == pygame.K_UP:
                paddle2_up = True
            if event.key == pygame.K_DOWN:
                paddle2_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                paddle1_up = False
            if event.key == pygame.K_s:
                paddle1_down = False
            if event.key == pygame.K_UP:
                paddle2_up = False
            if event.key == pygame.K_DOWN:
                paddle2_down = False

    if paddle1_up:
        y1-=10
        if y1<=0:
            y1=0

    if paddle1_down:
        y1+=10
        if y1>=515:
            y1=515
        
    if paddle2_up:
        y2-=10
        if y2<=0:
            y2=0
    if paddle2_down:
        y2+=10
        if y2>=515:
            y2=515
        
    if ball_pos[1] > display__size[1] - 30:
       
       
       ball_speed[1] = (ball_speed[1] * -1)

    elif ball_pos[1] < 0:
        
        
        ball_speed[1] = (ball_speed[1] * -1)



    if ball_pos[0] > display__size[0]:
        player2 += 1
       
        rally = 0
        
        
        ball_speed = pygame.math.Vector2(random.randint(-10, 11), random.randint(-10, 11))
        ball_pos = pygame.math.Vector2(385, 285)

    if ball_pos[0] < 0:
        player1 += 1
        
        rally = 0
        
        
        ball_speed = pygame.math.Vector2(random.randint(-10, 11), random.randint(-10, 11))
        ball_pos = pygame.math.Vector2(385, 285)
        
    if (0 < int(ball_pos[0]) <= 30) and (y1-100 < int(ball_pos[1]) <= y1 + 100):
        
        rally += 1
        
        

        ball_speed = (ball_speed * -1)
        ball_speed[0] = random.randint(1,11)
        ball_speed[1] = random.randint(-10,11)

    if (986 < int(ball_pos[0]) <= 1024 - 30) and (y2-100  < int(ball_pos[1]) <=y2 + 100):
        
        rally += 1
       
        
        ball_speed = (ball_speed * -1)
        ball_speed[0] = random.randint(-11, -1)
        ball_speed[1] = random.randint(-10, 11)

    rallyRender = rallyText.render(str(rally), 4, white)
    player1Render = rallyText.render(str(player1), 4, white)
    player2Render = rallyText.render(str(player2), 4, white)

    display.fill(black)

    display.fill(black)
    display.blit(bg, (0, 0))
    display.blit(paddle1, (x1, y1))
    display.blit(paddle2, (x2, y2))
    display.blit(ball, ball_pos)
    display.blit(player1Render, (570, 10))
    display.blit(player2Render, (420, 10))
    
    pygame.display.flip()
    clock.tick(60)
sys.exit()
