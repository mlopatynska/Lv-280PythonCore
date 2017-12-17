import datetime
year=input('Please type year \n')
mont=raw_input ('Please type month \n')
day=input ('Please type day \n')
try:
    print (str(datetime.date (year,int(mont),day)) + ' is the correct date mode')
except ValueError:
    print ('Incorrect input! Please enter year, month and day as digits, for example 2000 for year, 11 for month \
(November) and 11 for day (eleventh)!')