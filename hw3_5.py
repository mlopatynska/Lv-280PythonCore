k=input("Enter day year 1...365 - ")

if k in range(1,365,7): print("Monday")
elif k in range(2,365,7): print("Tuesday")
elif k in range(3,365,7): print("Wednesday")
elif k in range(4,365,7): print("Thursday")
elif k in range(5,365,7): print("Friday")
elif k in range(6,365,7): print("Saturday")
elif k in range(7,365,7): print("Sunday")
else: print"{} not 1...365".format(k)
