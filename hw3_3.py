a=input("Input a ")
b=input("Input b ")
c=input("Input c ")
D=b**2-4*a*c
print "Result {}x2+{}x+{}=0".format(a,b,c)
import math

if a==0: print "x={}".format(-c/b)
elif D>0:
    print "x1={}".format((-b+math.sqrt(D))/2*a)
    print "x2={}".format((-b-math.sqrt(D))/2*a)
elif D==0: print "x1={}".format(-b/2*a)
else: print "NOT Result"
    
