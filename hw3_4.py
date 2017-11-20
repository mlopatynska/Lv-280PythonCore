a=input('Input a=')
b=input('Input b=')
c=input('Input c=')

if a+b>c and a+c>b and b+c>a:
    print "P={}".format(a+b+c)
    import math
    p=(a+b+c)/2
    print "S={}".format(math.sqrt(p*(p-a)*(p-b)*(p-c)))
    
else: print 'no'
