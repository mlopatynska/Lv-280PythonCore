given_number = input("Please input a number\n")
sum = 0

for i in range(len(str(given_number))):
    sum += int(str(given_number)[i]) ** 3

# Alternative solution
#sum = eval("**3+".join(list(str(given_number)))+"**3")

print "The sum of cubed digits of {} = {}".format(given_number, sum)