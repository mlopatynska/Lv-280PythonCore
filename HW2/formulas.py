from math import *
x=float(raw_input("Enter variable X please:"))
y=float(raw_input("Enter variable Y please:"))
z=float(raw_input("Enter variable Z please:"))
i=1
print("a result="+str((sqrt(fabs(x-1))-(fabs(y)**(1/3.0)))/(1+x**2/2+y**2/4)))
print("b result="+str(x*atan(z)+exp((x+3)*-1))+'\n')

print("b result="+str((1+fabs(y-x)+sqrt(fabs(x-1))-(fabs(y)**(1/3.0)))/(1+x**2/2+y**2/4)))
#print(243**(1/5.0))