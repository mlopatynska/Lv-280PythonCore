import math
a=int(raw_input('pleace enter a:\n'))
b=int(raw_input('pleace enter b:\n'))
c=int(raw_input('pleace enter c:\n'))

D = b**2-4*a*c
if D > 0:
    x1=(-b+math.sqrt(D))/2*a
    x2=(-b-math.sqrt(D))/2*a
    print "result 1 is: {} & result 2 is: {}".format(x1,x2)
if D == 0:
    x=-b/2*a
    print "result is :{}".format(x)
if D <0:
    print "float root does not exist"