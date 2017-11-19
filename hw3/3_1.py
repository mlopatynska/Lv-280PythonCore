year1=int(raw_input("Enter year please:"))

if year1%4>0:
    print("This year is not a leap.")
elif (year1%100>0):
    print("It's a leap year.")
elif (year1%100==0) and (year1%400==0):
    print("It's a leap year.")
