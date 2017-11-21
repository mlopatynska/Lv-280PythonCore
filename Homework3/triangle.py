from math import *
a = input('Enter first side of the triangle\n')
b = input('Enter second side of the triangle\n')
c = input('Enter third side of the triangle\n')
if a <(b+c) and b < (a+c) and c <(b+a):
    P = a + b + c
    print ("Lenght  =", P)
    p = (a + b + c) / 2
    S = (sqrt(p*(p - a)*(p - b)*(p - c)))
    print ('Square =', S)
else:
    print ('Incorrect data')