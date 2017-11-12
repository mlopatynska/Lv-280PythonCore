import math

x=int(raw_input("pleace enter x:"))
y=int(raw_input("pleace enter y:"))
z=int(raw_input("pleace enter z:"))

a =(math.sqrt(x-1)/y - pow(abs(y),float(1/3)))/(1+(pow(x,2)/2)+(pow(y,2)/4))
print 'a=' , a
b =x*(math.atan(z)+pow(math.e,(-x-3)))
print 'b=' , b