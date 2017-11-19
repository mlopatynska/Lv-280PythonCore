from math import *
a=int(raw_input("Enter a please:"))
b=int(raw_input("Enter b please:"))
c=int(raw_input("Enter c please:"))

d=b*b-4*a*c
if d>0:
    print("x1="+str((-b+sqrt(d))/(2*a)))
    print("x2="+str((-b-sqrt(d))/(2*a)))
elif d==0:
    print('x='+str((-b /(2*a))))
else:
    print("There are not actual roots ")