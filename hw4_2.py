# -*- coding: cp1251 -*-
x=input("Enter Digit x = ")


counter=0

'''i=2
while i<=9:
    if float(x%i)!=0:
        i+=1
        counter+=1
    else: i+=1'''


for i in range(2,10):
    if float(x%i)!=0:
        counter+=1

print("{} - it's a prime digit" if counter==8
              else "{} - this іs not a prime digit" ).format(x)
