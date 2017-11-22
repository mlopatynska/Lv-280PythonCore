num = input("Enter number please:")
count = 0
for i in range(1,num,1):
    if num%i == 0:
        count +=1
if count>2:
    print("{} this number si NOT prime number".format(num))
else:
    print("{} this number si PRIME NUMBER".format(num))
