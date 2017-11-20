year=int(raw_input('pleace enter a year:\n'))
month=int(raw_input('pleace enter a month:\n'))
day=int(raw_input('pleace enter a day:\n'))

if year % 4 == 0 and month==2 and day==29:
    print 'Good Values. You chose a very rere day )'

elif month >= 12:
    print 'wrong  month !'
elif month==1 and day >31:
    print  'bad day'
elif month==2 and day >28:
    print  'bad day'
elif month==3 and day >31:
    print  'bad day'	
elif month==4 and day >30:
    print  'bad day'	
elif month==5 and day >31:
    print  'bad day'	
elif month==6 and day >30:
    print  'bad day'	
elif month==7 and day >31:
    print  'bad day'	
elif month==8 and day >31:
    print  'bad day'	
elif month==9 and day >30:
    print  'bad day'	
elif month==10 and day >31:
    print  'bad day'
elif month==11 and day >30:
    print  'bad day'
elif month==12 and day >31:
    print  'bad day'
	
else:
    print'Good Values !'