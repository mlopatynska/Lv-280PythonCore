import pygame, datetime, random
pygame.init()

done = False
clock = pygame.time.Clock()
n=6
screen = pygame.display.set_mode((n*100,n*100))
pygame.display.set_caption('My first game')

AQUA = (0,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
PURPLE = (128,0,128)
RED = (255,0,0)
GREY = (128,128,128)
GREEN = (0,255,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)




def boll(cell,color):
    pygame.draw.circle(screen,color,cell,40)

def square(cell,color):
    pygame.draw.rect(screen,color,[cell[0]-50,cell[1]-50,97,97])

def find(x,y):
    pxarray = pygame.PixelArray(screen)
    if pxarray[field[x][y][0],field[x][y][1]] == screen.map_rgb(GREEN):
        print 'GREEN'
    else: print 'not'

def line():
    k=0
    for i in range(n):
        for j in range(n):
            if find(i,j)==True: k+=1

field = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        field[i][j]=[50+(i*100),50+(j*100)]



for i in range(n):
    for j in range(n):
        square(field[i][j],GREY)

x=random.randint(0,5)
y=random.randint(0,5)
boll(field[x][y],GREEN)

l_time=0



while not done:
    for event in pygame.event.get():
        clock.tick()

        if event.type == pygame.QUIT: 
            done = True 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x-1>=0: x-= 1
                else: x=x
                boll(field[x][y],GREEN)
                square(field[x+1][y],GREY)
            elif event.key == pygame.K_RIGHT:
                if x+1<n: x+= 1
                else: x=x
                boll(field[x][y],GREEN)
                square(field[x-1][y],GREY)
            elif event.key == pygame.K_DOWN:
                if y+1<n: y+= 1
                else: y=y
                boll(field[x][y],GREEN)
                square(field[x][y-1],GREY)
            elif event.key == pygame.K_UP:
                if y-1>=0: y -= 1
                else: y=y
                boll(field[x][y],GREEN)
                square(field[x][y+1],GREY)

            
        elif event.type == pygame.KEYUP:
            print x,y
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            print("User pressed a mouse button")

	
#    screen.fill(WHITE)
    if pygame.time.get_ticks() - l_time > 3000:
        l_time = pygame.time.get_ticks()    
        x=random.randint(0,5)
        y=random.randint(0,5)
        boll(field[x][y],GREEN)
        find(x,y)



    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
