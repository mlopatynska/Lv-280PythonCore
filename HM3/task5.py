#znahodzhennia dnia tyzhnia
k = int(raw_input("Please, input a day of the year: "))
if k not in range(1,366):
    print ('The value does not match the condition of the task')
else:
     n = float(k % 7)
     if n == 0:
        print "It is Sunday"
     elif n == 6:
        print "It is Saturday"
     elif n == 5:
        print "It is Friday"
     elif n == 4:
        print "It is Thursday"
     elif n == 3:
        print "It is Wednesday"
     elif n == 2:
        print "It is Tuesday"
     else:
        print "It is Monday"
