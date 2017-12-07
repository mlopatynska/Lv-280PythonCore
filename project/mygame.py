import pygame, random

pygame.init()

#variables to be used

#here we define variables with colours to use them farther
green=(0,128,0)
purple=(128,0,128)
black = (  0,   0,   0)
white = (255, 255, 255)
blue =  (  0,   0, 255)
red = (255, 0, 0)
brown = (255,248,220)

Display = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Project game')
#pygame.mouse.set_visible(False) # here we make mouse pointer invisible

# images
back_image = pygame.image.load("mt-sample-background.jpg").convert() #must go after setting display mode!
player_image = pygame.image.load("spaceship-icon.png").convert()
alien = pygame.image.load("clipart-alien-ffce.png").convert()
player_image.set_colorkey(white) # makes white colour transparent
alien.set_colorkey(black)

# sounds
click_sound = pygame.mixer.Sound("laser1.ogg")

# spaceship movement
# Speed in pixels per frame
x_speed = 0
y_speed = 0
# Initial position
x_coord = 10
y_coord = 350

#alien movement
# Initial position
alienx_coord = 1200
alieny_coord = random.randrange(0, 570)
# Speed in pixels per frame
alienx_speed = -3

done = False
clock = pygame.time.Clock()


# main game loop
while done == False:

    Display.blit(back_image, [0, 0])


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: #when we press the key
            if event.key == pygame.K_LEFT: #pressing left arrow key
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            elif event.key == pygame.K_SPACE:
                click_sound.play() # shooting sound
                pygame.draw.line(Display, purple, [x_coord+128, y_coord+64], [x_coord+478, y_coord+64], 3) #shooting animation
        elif event.type == pygame.KEYUP: #when we let key go
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed
    #print (x_coord,y_coord)

    # limit the movement of object
    if x_coord < -2:
        x_coord = -2
    elif y_coord <= -19:
        y_coord = -19
    elif y_coord >= 596:
        y_coord = 596

    Display.blit(player_image, [x_coord, y_coord])

    Display.blit(alien, [alienx_coord, alieny_coord])
    alienx_coord = alienx_coord+alienx_speed
    if alienx_coord < 0:
        alienx_coord = 1200
        Display.blit(alien, [alienx_coord, alieny_coord])
    print (alienx_coord, alieny_coord)




    pygame.display.flip()  # updates full display
    clock.tick(30)
pygame.quit()  # ends the game when loop is over