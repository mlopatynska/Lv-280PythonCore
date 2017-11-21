year = input("Enter year:")
try:
    year = int(year)
    if not (year % 4) and (year % 100):
        print("It is a leap year")
    elif (year % 400):
        print("It is not a leap year")
    else:
        print("Error")
except:
    print("Exception")