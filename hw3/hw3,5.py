k=input('Please type any day of the year, from 1 to 365.\n')

if k%7==1:
    print ("the {}-th day of this hypothetical year is Monday".format(k))
elif k%7==2:
    print ("the {}-th day of this hypothetical year is Tuesday".format(k))
elif k%7==3:
    print ("the {}-th day of this hypothetical year is Wednesday".format(k))
elif k%7==4:
    print ("the {}-th day of this hypothetical year is Thursday".format(k))
elif k%7==5:
    print ("the {}-th day of this hypothetical year is Friday".format(k))
elif k%7==6:
    print ("the {}-th day of this hypothetical year is Saturday".format(k))
else:
    print ("the {}-th day of this hypothetical year is Sunday".format(k))