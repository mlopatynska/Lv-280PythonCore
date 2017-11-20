import calendar
year=input('Please enter any year AD \n')
if calendar.isleap(year):
    print ("It's a leap year!")
else:
    print ('This is not a leap year!')