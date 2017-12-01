import random

x = 5
y = 5
array = []
for i in range(x):
    array.append([])
    for j in range(y):
        array[i].append([random.randint(0, 100)])
print('Matrix')
for u in range(x):
    print(array[u])
z = 0
for a in range(x):
    for b in range(y):
        if array[a][b] > z:
            z = array[a][b]
print("max.number=", z)



