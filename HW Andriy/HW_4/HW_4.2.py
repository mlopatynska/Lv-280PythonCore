day = input("Please enter day ")
month = input("Please enter month (number) ")
year = input("Please enter year ")

day_correct_format = True
month_correct_format = True
year_correct_format = True

if month in [1, 3, 5, 7, 8, 10, 12]:
    if day not in range(1, 31):
        day_correct_format = False
elif month in [4, 6, 9, 11]:
    if day not in range(1, 30):
        day_correct_format = False
elif month == 2:
    if day not in range(1, 28):
        day_correct_format = False
else:
    month_correct_format = False

if year not in range(1900, 2100):
    year_correct_format = False

if day_correct_format and month_correct_format and year_correct_format:
    print "The date format is correct"
else:
    print "The date format is not correct"