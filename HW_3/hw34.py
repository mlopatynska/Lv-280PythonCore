import math
a=float(raw_input('enter side a:'))
b=float(raw_input('enter side b:'))
c=float(raw_input('enter cide c:'))


if a >= b+c :
    print 'not triangle'
elif b >= a+c :
    print ' not triangle'
elif c >= a+b :
    print 'not triangle'
else :
    P=(a+b+c)/2
    S=math.sqrt(P*(P-a)*(P-b)*(P-c))
    print "triangle P={} , S={}".format(P,S)