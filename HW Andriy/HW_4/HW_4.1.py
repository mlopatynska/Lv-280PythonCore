year = input("Please enter year\n")

print ""

if year % 100 == 0 and year % 400 != 0:
    print "It's not a leap year!"
elif year % 4 == 0:
    print "It's a leap year!"
else:
    print "It's not a leap year!"