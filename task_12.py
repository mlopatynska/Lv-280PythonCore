
a = int(input ("please enter a: "))
b = int(input ("please enter b: "))
c = int(input ("please enter c: "))
if a > (b+c):
    print ("this is not a triangle")
elif b > (a+c):
    print ("this is not a triangle")
elif c > (a+b):
    print ("this is not a triangle")
else:
    P=a+b+c
    print 'perimetr of this triangle is =', P
    pivP = (a + b + c) / 2
    S = ((a+b+c)*(b+c-a)*(a+c-b)*(a+b-c)) / 4
    print 'square of this triangle is =', S