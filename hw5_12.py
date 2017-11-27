#---------5_1-------------
import random
a = [random.uniform(1, 100) for x in range(30)]
b = [random.uniform(1, 100) for x in range(30)]
c = [random.uniform(1, 100) for x in range(30)]
#a = [3 for x in range(30)]
#b = [2 for x in range(30)]
#c = [1 for x in range(30)]
x = input('Enter x = ')
y = input('Enter y = ')
z = input('Enter z = ')

def sum_of_products (p1,p2):
    S=0
    for i in range(len(p1)):
        S+=p1[i]*p2**(len(p1)-i)
    return S

print(sum_of_products(a,x)**2-sum_of_products(b,y))/(sum_of_products(c,x+z)
                                if sum_of_products(c,x+z)!=0 else 'Restart' )
   
#-------------5_2--------------
n=input('Enter n = ')
m=input('Enter m = ')

def f(d):
    p=1
    if d==0 and d==1: return float(p)
    for i in range(1,d+1): p*=i
    return float(p)

print (float((f(n)*f(m))/f(n+m)))
