print "Enter digits."
year=input("Year ")
month=input("Month ")
day=input("Day ")
def lear(year):
    if year%4==0:
        if year%100!=0 or (year%100==0 and year%400==0):
            result=True
    else:
        result=False
    return result

if len(str(year))!=4:
    print "This is NOT correctly year!!!"
elif month not in range(1,13):
    print "This is NOT correctly month!!!"
elif day not in range(1,32):
    print "This is NOT correctly day!!!"
elif month==2:
    if (day in range(1,30)and lear(year)==True)or(
            day in range(1,29)and lear(year)==False):
        print("{},{},{} - it's correctly Date").format(year,month,day)
    else: "This is NOT correctly date!!!"
else: 
    print("{},{},{} - it's correctly date").format(year,month,day)

# при вводі некоректн дати Наприк: 2016,2,30 - else пропускає ??????
import datetime
date = datetime.datetime.now()


print("{},{},{}-current date" if date.year==year and date.month==month
        and date.day==day else "{},{},{}-not current date").format(year,month,day)

    
