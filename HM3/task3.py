#kvadratne rivniannia
from math import sqrt
a=int(raw_input('Please enter a='))
b=int(raw_input('Please enter b='))
c=int(raw_input('Please enter c='))

print ('{}*x^2+{}*x+{}=0').format(a, b, c)
d=(b**2)-(4*a*c)
print ('D = {}').format(d)
if d>0:
   x1=((-b)+(sqrt(d)))/(2*a)
   x2=((-b)-(sqrt(d)))/(2*a)
   print ('x1= {}').format(x1)
   print ('x2= {}').format(x2)
elif d==0:
   x3=-b/2*a
   print ('x= {}').format(x3)
elif d<0:
   print ('the equation has no answer')