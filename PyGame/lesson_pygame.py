import pygame
pygame.init()

done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('My first game')
font = pygame.font.SysFont('Calibri', 25, True, False)

background_image = pygame.image.load("saturn_family1.jpg")
player_image = pygame.image.load("playerShip1_orange.png")

click_sound = pygame.mixer.Sound("Ok.wav")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

i,x,y,z,w = 0,400,300,400,300
# -------- Main Program Loop -----------
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_DOWN:
                y += 10
            elif event.key == pygame.K_UP:
                y -= 10
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
            print("User pressed a mouse button")
        elif event.type == pygame.MOUSEMOTION:
            player_position = pygame.mouse.get_pos()
            z = player_position[0]
            w = player_position[1]
            print("User pressed a mouse move")

    screen.fill(BLUE)
    screen.blit(background_image, [0, 0])
    screen.blit(player_image, [z, w])

    pygame.draw.rect(screen,RED,[0,0,400,300],15)
    pygame.draw.line(screen,WHITE,[0,0],[400,300],10)

    pygame.draw.circle(screen,GREEN,[x,y],30)
    if x > 800:
        x = 0
    elif x < 0:
        x = 800
    if y > 600:
        y = 0
    elif y < 0:
        y = 600


    for j in range(0,800,30):
        pygame.draw.rect(screen, WHITE, [j, 580, 20, 20])

    pygame.draw.rect(screen, RED, [i, 580, 20, 20])
    if i > 800:
        i = 0
    else:
        i += 10

    text = font.render("My text should br here", True, WHITE)
    screen.blit(text, [250, 250])


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
