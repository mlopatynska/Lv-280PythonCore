from math import sqrt
a=int(raw_input("Enter a side please:"))
b=int(raw_input("Enter b side please:"))
c=int(raw_input("Enter c side please:"))

if (a<c+b) and (c<a+b) and (b<c+a):
    print("triangle perimeter is: "+str(a+b+c))
    p=(a+b+c)/2
    print("triangle area is:      "+str(sqrt(p*(p-a)*(p-b)*(p-c))))
else:
    print("Triangle is imposible whith such sides")