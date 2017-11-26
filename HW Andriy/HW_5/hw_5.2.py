given_number = input("Please input a number\n")

for i in range(2, given_number+1):
    if i == given_number:
        print "This is a prime number"
    elif given_number % i == 0:
        print "This is not a prime number"
        break
    elif given_number % i != 0:
        continue
