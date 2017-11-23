num = input("Enter number please:")

sum=0
str_=str(num)
for i in range(len(str_)):
    sum+=int(str_[i])**3

print("Sum of cubic digits of {}={}".format(num,sum))