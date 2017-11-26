given_number = input("Please input a number\n")
fibonacci = [1]

for i in range(1, given_number):
    if i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print "The first {} fibonacci numbers are {}".format(given_number, str(fibonacci).replace("[", "").replace("]", ""))