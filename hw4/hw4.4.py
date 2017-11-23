num=raw_input('Enter any number\n')
sum=0
if num[0] == '-':
    for let in range(1,len(num)):
        sum = sum + -int(num[let]) ** 3
else:
    for let in range(len(num)):
        sum = sum + int(num[let]) ** 3
print (sum)
