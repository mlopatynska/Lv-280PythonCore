# This Python file uses the following encoding: utf-8
import pygame, random

pygame.init()

# variables with colours
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
pygame.mixer.music.load("01_brad_fiedel_theme_from_the_terminator_myzuka.mp3")
pygame.mixer.music.play()

class Spaceship(object):
    def __init__(self):
        # Speed in pixels per frame
        self.x_speed = 0
        self.y_speed = 0
        # Initial position
        self.x_coord = 10
        self.y_coord = 350
        # initial position of muzzle
        self.xmuzzle = self.x_coord + 122 # координати дула лазера
        self.ymuzzle = self.y_coord + 61
    def move(self):
        if event.type == pygame.KEYDOWN:  # when we press the key
            if event.key == pygame.K_LEFT: # pressing left arrow key
                self.x_speed = -3
            elif event.key == pygame.K_RIGHT:
                self.x_speed = 3
            elif event.key == pygame.K_UP:
                self.y_speed = -3
            elif event.key == pygame.K_DOWN:
                self.y_speed = 3
        elif event.type == pygame.KEYUP: # when we let key go
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.y_speed = 0
        # Move the object according to the speed vector.
        self.x_coord += self.x_speed
        self.y_coord += self.y_speed
        # limit the movement of object
        if self.x_coord < -2:
            self.x_coord = -2
        elif self.y_coord <= -19:
            self.y_coord = -19
        elif self.y_coord >= 596:
            self.y_coord = 596
    def blit(self):
        Display.blit(player_image, [self.x_coord, self.y_coord])
    def shoot(self):
        if event.type == pygame.KEYDOWN:  # when we press the key
            if event.key == pygame.K_SPACE:
                click_sound.play()  # shooting sound
                pygame.draw.rect(Display, purple, [self.xmuzzle, self.ymuzzle, 50, 5])  # laser
        self.xmuzzle = self.x_coord + 122 # here we override the initial positions to make sure it's changed with
        # spaceship movements
        self.ymuzzle = self.y_coord + 61

class Laser(Spaceship):
    def __init__(self):
        super(Laser, self).__init__() #here we initialize both attributes of parent class and child class
        self.las_speed = 10
    def blit(self):
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            print self.xmuzzle
            if self.xmuzzle <= 1200:  # if laser beam reaches the end of screen - it must stop!
                pygame.draw.rect(Display, purple, [self.xmuzzle, self.ymuzzle, 50, 5])  # laser
    def move(self):
        # limit of laser movements
            self.xmuzzle = self.xmuzzle + self.las_speed









spaceship = Spaceship() # instatiation
laser = Laser()

#alien movement
# Initial position
alienx_coord = 1200

aliens = [[alienx_coord, random.randrange(0, 570, 128)] for nl in range(5)] # nested list comprehension!
# print aliens
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

    spaceship.blit()
    spaceship.move()
    spaceship.shoot()
    laser.blit()
    laser.move()

    # aliens' movements and appearing
    for nl in range(len(aliens)):
        Display.blit(alien, aliens[nl])
        aliens[nl][0] = aliens[nl][0] + alienx_speed
        if aliens[nl][0] < 0:
            aliens[nl][0] = alienx_coord
            aliens[nl][1] = random.randrange(0,570, 128)
            Display.blit(alien, [aliens[nl][0], aliens[nl][1]])


    pygame.display.flip()  # updates full display
    clock.tick(30)
pygame.quit()  # ends the game when loop is over