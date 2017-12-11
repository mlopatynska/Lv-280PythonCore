import pygame, time, random
pygame.init()

done = False
clock = pygame.time.Clock()
N=6

screen = pygame.display.set_mode((N*100,N*100))

pygame.display.set_caption('My first game')
font = pygame.font.SysFont('Calibri', N*15, True, False)

COLOR = [(128,128,128),(0,255,0),(255,0,0),(0,0,255)]

#AQUA = (0,255,255)
BLACK = (0,0,0)
#BLUE = (0,0,255)
#PURPLE = (128,0,128)
#RED = (255,0,0)
#GREY = (128,128,128)
#GREEN = (0,255,0)
WHITE = (255,255,255)
#YELLOW = (255,255,0)


SCORE = 2000
LEVEL = 50000
field = [[0 for i in range(N)] for j in range(N)]
last_time=0
level_time=0


def boll(i,j,c):
    pygame.draw.circle(screen,COLOR[c],[field[i][j][0],field[i][j][1]],40)
    field[i][j][2]=c

def square(i,j,c=COLOR[0]):
    pygame.draw.rect(screen,c,[field[i][j][0]-50,field[i][j][1]-50,97,97])
    field[i][j][2]=0

def emptyfield():
    screen.fill(BLACK)
    for i in range(N):
        for j in range(N):
            field[i][j]=[50+(i*100),50+(j*100),0]
            square(i,j)
    
def findline(i,j):
    if i-2>=0:    
        if field[i-2][j][2] == field[i-1][j][2] == field[i][j][2]:
            square((i-2),j)
            square((i-1),j)
            square(i,j)
    if i-1>=0 and i+1<N:
        if field[i-1][j][2] == field[i][j][2] == field[i+1][j][2]:
            square(i-1,j)
            square(i,j)
            square(i+1,j)
    if i+2<N:
        if field[i][j][2] == field[i+1][j][2] == field[i+2][j][2]:
            square(i,j)
            square(i+1,j)
            square(i+2,j)
    if j-2>=0:    
        if field[i][j-2][2] == field[i][j-1][2] == field[i][j][2]:
            square(i,j-2)
            square(i,j-1)
            square(i,j)
    if j-1>=0 and j+1<N:
        if field[i][j-1][2] == field[i][j][2] == field[i][j+1][2]:
            square(i,j-1)
            square(i,j)
            square(i,j+1)
    if j+2<N:
        if field[i][j][2] == field[i][j+1][2] == field[i][j+2][2]:
            square(i,j)
            square(i,j+1)
            square(i,j+2)

def findover():
    for i in range(N):
        for j in range(N):
            if field[i][j][2]==0:
                return True
    return False

def gameover():
    text = font.render("GAME OVER", True, WHITE)
    screen.blit(text, [70, 200])
    

#screen.fill(WHITE)
#pygame.draw.rect(screen,GREEN,[n*20,m*25,n*50,m*20])
#text = font.render("GAME", True, BLACK)
#screen.blit(text, [n*30, n*40])
#pygame.draw.rect(screen,GREEN,[n*60,m*25,n*50,m*20])
#text = font.render("GAME OVER", True, BLACK)
#screen.blit(text, [n*30, n*40])


#------picture field------
emptyfield()

x,y,z=random.randint(0,N-1),random.randint(0,N-1),random.randint(1,3)
boll(x,y,z)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
            gameover() 
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x-1>=0 and field[x-1][y][2] == 0:
                    x-= 1
                    boll(x,y,z)
                    square((x+1),y)
                
            elif event.key == pygame.K_RIGHT:
                if x+1<N and field[x+1][y][2] == 0:
                    x+= 1
                    boll(x,y,z)
                    square((x-1),y)
                
            elif event.key == pygame.K_DOWN:
                if y+1<N and field[x][y+1][2] == 0:
                    y+= 1
                    boll(x,y,z)
                    square(x,(y-1))
                
            elif event.key == pygame.K_UP:
                if y-1>=0 and field[x][y-1][2] == 0:
                    y -= 1
                    boll(x,y,z)
                    square(x,(y+1))
                

            
#        elif event.type == pygame.KEYUP:
#            print x,y
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            print("User pressed a mouse button")

	

    if pygame.time.get_ticks() - last_time > SCORE:
            
        x,y,z=random.randint(0,N-1),random.randint(0,N-1),random.randint(1,3)
        if field[x][y][2]==0:
            last_time = pygame.time.get_ticks()
            boll(x,y,z)
        else:
            if findover()==False: 
                done = True
                gameover() 
        if last_time-level_time>LEVEL:
            level_time=last_time
            SCORE-=500

#            text = font.render("LEVEL "+str(SCORE/500-(SCORE/500-1)), True, WHITE)
#            screen.blit(text, [200, 300])            
#            emptyfield()   
    findline(x,y)


    
    pygame.display.update()
    clock.tick(10)

time.sleep(2)
pygame.quit()
quit()
