from math import *
a = input('enter data of equation\n')
b = input('enter data of equation\n')
c = input('enter data of equation\n')
print(a,"*x*x+",b,'*x+',c, '=0')
d = ((b*b)-(4*a*c))
if d < 0:
        print('This equation doesn`t have a real solution')

if d == 0:
    x = (-b)/2*a
    print('This equation has one real solution!')
    print('x=', x)
elif d > 0:
    x1 = (((-b) + ((sqrt(d)) / 2 * a)))
    x2 = ((-b) - ((sqrt(d)) / 2 * a))
    print('This equation has two real solution!\n')
    print('x1=', x1, 'x2=', x2)
