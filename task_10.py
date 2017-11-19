day = int(input("please enter a day(1-31): "))
month = int(input("please enter a month(1-12): "))
year = int(input("please enter a year (4-digit number): "))
if month == 1 and day > 31:
    print ("you entered a wrong day, please try again!")
elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("it's a leap year. in leap year we have 29 days in fabruary")
    print 'you entered this date: ', day, '-', month, '-', year
elif month == 2 and day > 28:
    print ("you entered a wrong day, please try again!")
elif month == 3 and day > 31:
    print ("you entered a wrong day, please try again!")
elif month == 4 and day > 30:
    print ("you entered a wrong day, please try again!")
elif month == 5 and day > 31:
    print ("you entered a wrong day, please try again!")
elif month == 6 and day > 30:
    print ("you entered a wrong day, please try again!")
elif month == 7 and day > 31:
    print ("you entered a wrong day, please try again!")
elif month == 8 and day > 31:
    print ("you entered a wrong day, please try again!")
elif month == 9 and day > 30:
    print ("you entered a wrong day, please try again!")
elif month == 10 and day > 31:
    print ("you entered a wrong day, please try again!")
elif month == 11 and day > 30:
    print ("you entered a wrong day, please try again!")
elif month == 12 and day > 31:
    print ("you entered a wrong day, please try again!")
elif day <= 0:
    print ("you entered a wrong day. try again!!!")
elif month <= 0 or month > 12:
    print ("you entered a wrong month. try again!!!")
elif year < 0:
    print ("you entered a wrong year. try again!!!")
elif year == 0:
    print 'you entered this date: ', day, '-', month, '-', '0000'
else:
    print 'you entered this date: ', day, '-', month, '-', year


