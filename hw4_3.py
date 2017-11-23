# Fibonachi N
N=input('Enter N =')

First=0
Next=1
print First
for i in range(2,N+1):
    print Next
    First,Next=Next,(First+Next)


