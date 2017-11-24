from math import exp,factorial,fabs

a=input("Enter a please:")
b=input("Enter b please:")
h=input("Enter step please:")
E=0.00001
print ("X           S           Y           Pohybka")
x = a
while x < b :
    y = (x-1)*exp(x)+1
    s = 0
    k = 0
    p = 1
    №print("{}       {}      {}      {}".format(x,s,y,p))
    while p>E:
        s+=(1/float(factorial(k)*(k+2)))*x**(k+2)
        p=fabs((s-y)/y)*100
        k+=1
    x += h
    print("{}       {}      {}      {}".format(x,s,y,p))