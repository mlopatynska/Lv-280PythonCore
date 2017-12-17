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

#scores
score = 0

#text variables
font = pygame.font.Font(None, 25)



# images
back_image = pygame.image.load("mt-sample-background.jpg").convert() #must go after setting display mode!
player_image = pygame.image.load("spaceship-icon.png").convert()
alien_image= pygame.image.load("clipart-alien-ffce.png").convert()
player_image.set_colorkey(white) # makes white colour transparent
alien_image.set_colorkey(black)

# sounds
click_sound = pygame.mixer.Sound("laser1.ogg")
pygame.mixer.music.load("01_brad_fiedel_theme_from_the_terminator_myzuka.mp3")
pygame.mixer.music.play()
hit_sound = pygame.mixer.Sound("phaserUp1.ogg")
bite_sound = pygame.mixer.Sound("zap2.ogg")

# global variable to start shooting
fire = True
# global variable for coordinate updating
x_coord = 0
y_coord = 0
# global variable with aliens
aliens = []
#variable to stop laser sound
target_hit = False

class Spaceship(object):
    def __init__(self):
        # Speed in pixels per frame
        self.x_speed = 0
        self.y_speed = 0
        # Initial position
        self.x_coord = 10
        self.y_coord = 350
        # initial position of muzzle
        self.xmuzzle = self.x_coord + 122  # координати дула лазера
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
        global x_coord # here we override the global variable x_coord to make sure its value is updated
        x_coord = self.x_coord
        global y_coord # here we override the global variable y_coord
        y_coord = self.y_coord
    def shoot(self):
        # position of muzzle is updated when x_coord and y_coord are overriden
        self.xmuzzle = x_coord + 122  # координати дула лазера
        self.ymuzzle = y_coord + 61
        if event.type == pygame.KEYDOWN:  # when we press the key
            if event.key == pygame.K_SPACE:
                click_sound.play()  # shooting sound

class Laser(Spaceship):
    def __init__(self):
        super(Laser, self).__init__()
        self.las_speed = 10
    def blit(self):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            global fire
            fire = False
            self.xmuzzle = x_coord + 122 # here we override the coordinates of muzzle according to new position
            self.ymuzzle = y_coord + 61  # of the spaceship, to avoid getting old position from inherited variables
    def move(self):
        global fire
        if fire == False:
            # limit of laser movements
            pygame.draw.rect(Display, purple, [self.xmuzzle, self.ymuzzle, 50, 5])  # laser
            self.xmuzzle = self.xmuzzle + self.las_speed
        if self.xmuzzle > 1192:
            # print '--', self.xmuzzle
            global fire
            fire = True
            self.xmuzzle = x_coord + 122
            self.ymuzzle = y_coord + 61
    def hit(self):
        for alien_ in range(len(aliens)):
            if target_hit == False:
                # print 'start', self.xmuzzle
                if self.xmuzzle + 50 >= aliens[alien_][0] and self.xmuzzle < 1192: # checking if laser hit an alien, i.e.
                # if x coordinates of laser reached the x coordinates of any alien
                    # print "!!!"
                    if self.ymuzzle in range(aliens[alien_][1], aliens[alien_][1] + 129): # cheking if y coordinates of
                        # a laser are the same as y coordinates of an alien + its height (128 pixels)
                        hit_sound.play()
                        global score
                        score = score + 1 # adding scores when an alien is hit
                        global target_hit
                        target_hit = True # variable to stop playing sound of hit after one time
                        global fire
                        fire = True # here we stop drawing laser once it hits the alien
            if target_hit == True:
                # print "current x_muzzle!", self.xmuzzle
                if self.xmuzzle >= 1192: # if the laser beam reached the end of
                    # print self.xmuzzle, "final"
                    target_hit = False

class Aliens(Laser):
    def __init__(self):
        super(Aliens, self).__init__()
        # Initial position
        self.alienx_coord = 1200
        # Speed in pixels per frame
        self.alienx_speed = -3
    def create(self):
        global aliens
        if len(aliens) < 1:
            # self.alienx_coord + random.randrange(1,250,128) prevents aliens from appearing in one column
            aliens = [[self.alienx_coord + random.randrange(1,250,128), random.randrange(0, 570, 128)] for nl in range(5)]  # nested list comprehension!
    def blit(self,aliens):
        # aliens' movements and appearing
        for nl in range(len(aliens)):
            Display.blit(alien_image, aliens[nl])
            aliens[nl][0] = aliens[nl][0] + self.alienx_speed
            if aliens[nl][0] < 0:
                aliens[nl][0] = self.alienx_coord
                aliens[nl][1] = random.randrange(0, 570, 128)
                Display.blit(alien_image, [aliens[nl][0], aliens[nl][1]])
    def bite(self, aliens):
        # print aliens, "!!!!!!!!!!!!!!!!!!!!!!!!"
        for al in range(len(aliens)):
            # print aliens[al][0]
            if aliens[al][0] <= self.x_coord + 128:
                print aliens[al][0]
                print self.x_coord
                print "!!!!!!!!!!!!!!!!!!!!!!!!"
                bite_sound.play()






spaceship = Spaceship() # instatiation
laser = Laser()
alien = Aliens()



done = False
clock = pygame.time.Clock()

# main game loop
while done == False:

    Display.blit(back_image, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pygame.time.wait(5000)  # the game is paused for 5000 milliseconds (5 seconds)



    spaceship.blit()
    spaceship.move()
    spaceship.shoot()
    laser.blit()
    laser.move()
    laser.hit()
    text = font.render("You hit the alien " + str(score) + " times!", True, green) # writing scores on display
    Display.blit(text, [10, 10])
    alien.create()
    alien.blit(aliens)
    alien.bite(aliens)




    pygame.display.flip()  # updates full display
    clock.tick(30)
pygame.quit()  # ends the game when loop is over
