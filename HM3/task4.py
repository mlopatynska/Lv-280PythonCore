#vyznachennia perymetra i ploshchi trykutnyka
from math import sqrt

a=int(raw_input('Please enter side a: '))
b=int(raw_input('Please enter side b: '))
c=int(raw_input('Please enter side c: '))
if ((a<b+c) and (b<a+c) and (c<a+b)):
    p=a+b+c
    p1=p/2
    print ('P= {}').format(p)
    s=sqrt(p1*(p1-a)*(p1-b)*(p1-c))
    print ('S= {}').format(s)
else:
    print ('It is can\'t be a triangle')