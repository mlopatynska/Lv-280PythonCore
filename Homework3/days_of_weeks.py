a = input("Enter number of day of the year\n")
if a not in range (1,365):
    print ('You enter incorrect data')
else:
    if a%7==1:
        print ('You chose Monday')
    elif a%7==2:
        print ('You chose Tuesday')
    elif a%7==3:
        print ('You chose Wensday')
    elif a%7==4:
        print ('You chose Thursday')
    elif a%7==5:
        print ('You chose Friday')
    elif a%7==6:
        print ('You chose Saturday')
    elif a%7==0:
        print ('You chose Sunday')

