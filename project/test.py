import random
x_alien = 1150
y_alien = random.randint(0, 680)
move_left = 1
aliens=[]
for i in range(10): # here we say that there are 10 aliens
    y_alien = random.randint(0, 680)
    aliens.append([x_alien, y_alien])
    print aliens
for al in range(len(aliens)):
       print (x_alien, aliens[al][1])
