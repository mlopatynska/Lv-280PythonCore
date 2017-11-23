digit = input("please enter a digit: ")
my_range = range(1000, 10000)
for i in my_range:
    sum = (i/1000)+((i/100)%10)+((i/10)%10)+(i%10)
    if sum == digit:
        print i
    else:
        i += 1
print 'end of the program'
