n = int(input(" Enter a number: "))
res,mass=0,[]
for x in range (1000,10000):
    for symbol in str(x):
        print(str(x))
        res=res+int(symbol)
    if n == res:
        mass.append(x)
    res=0  
print(mass) 
