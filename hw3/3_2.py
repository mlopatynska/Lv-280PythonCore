import datetime

today = datetime.datetime.now()

SMALL_MONTH=(4, 6, 9, 11)

year1=int(raw_input("Enter year please:"))
month1=int(raw_input("Enter month please:"))
day1=int(raw_input("Enter day please:"))



if (year1>2017) or (year1<1):
    print("Wrong year!!!")
elif(month1>12) or (month1<1):
    print("Wrong month!!!")
elif (day1==(31)) and (month1 in range(SMALL_MONTH)):
    print("Wrong days count. This month has 30 days")
elif (day1 in range(30,32)) and (month1==2):
    print("Wrong days count. This month has 28 or 29 days")
elif (day1==today.day) and (month1==today.month) and (year1==today.year):
    print("You entered today date :) !!!")
else:
    print("Your date is: "+str(day1)+'.'+str(month1)+'.'+str(year1))