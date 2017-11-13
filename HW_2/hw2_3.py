import math

x=int(raw_input("pleace enter x: "))
y=int(raw_input("pleace enter y: "))
z=int(raw_input("pleace enter z: "))

a =(math.sqrt(abs(x-1))/y - pow(abs(y),float(1/3)))/(1+(pow(x,2)/2)+(pow(y,2)/4))
b =x*(math.atan(z)+pow(math.e,(-x-3)))
print '\na=',a  ,' b=',b

b_a=3+pow(math.e,y-1)/(1+pow(x,2)*abs(y-math.tan(z)))
b_b=1+abs(y-x)+pow(y-x,2)/2+pow(abs(y-x),3)/3
print 'b_a=',x  ,' b_b=',b_b

c_a=(1+y)*(x+y/(pow(x,2)+4)/(pow(math.e,-x-2)+1/(pow(x,2)+4)))
c_b=(1+math.cos(y-2))/(pow(x,4)/2+pow(math.sin(z),2))
print 'c_a=',c_a  ,' c_b=',c_b