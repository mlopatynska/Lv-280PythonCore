year=input('Input year ')

if year%4==0:
    if year%100!=0 or (year%100==0 and year%400==0):
        print "It's a leap year!"
else:
    print "This is not a leap year!"
