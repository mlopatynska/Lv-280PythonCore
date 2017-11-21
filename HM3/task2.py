#perevirka korektnosti vvodu znachen'
m31=['2','4', '6', '5', '9', '11']
d = int(raw_input("Day: "))
m = int(raw_input("Month: "))
y = int(raw_input("Year: "))

if m==2 and d==29 and y%4!=0:
    print 'value incorrect'
elif m==2 and d==30:
    print 'value incorrect'
elif d==31:
    if m not in m31:
       print 'value incorrect'
    elif (y<0) or (m not in range(1,13)) or (d not in range(1,32)):
       print ('value incorrect')
    elif d==31 and m not in m31:
        print 'value incorrect'
    else:
       print "date is correct"
else:
    print "date is correct"
