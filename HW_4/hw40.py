result = int(raw_input("Please enter en integer: "))
for i in range(1000,10000):
    sum = 0
    number = i
    while number:
        last_digit = number % 10
        number = number / 10
        sum = sum + last_digit
    if sum == result:
        print "Sum {} is a numbers: {}".format(result,i) 