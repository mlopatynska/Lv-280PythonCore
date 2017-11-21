day = input("Please enter a number of a day in a year (in range 1 to 365) to find out which day of the week is it "
            "(assuming January 1 is Monday)\n")

print ""

if day > 365 or day < 1:
    print "This is not a number of a day in a year"
elif day in range(1, 366, 7):
    print "It's Monday!"
elif day in range(2, 366, 7):
    print "It's Tuesday!"
elif day in range(3, 366, 7):
    print "It's Wednesday!"
elif day in range(4, 366, 7):
    print "It's Thursday!"
elif day in range(5, 366, 7):
    print "It's Friday!"
elif day in range(6, 366, 7):
    print "It's Saturday!"
elif day in range(7, 366, 7):
    print "It's Sunday!"
else:
    print "Oops, it seems like Andriy made a mistake"