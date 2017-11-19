import math
print ("let's solve a quadratic equation")
a = int(input ("please enter a: "))
b = int(input ("please enter b: "))
c = int(input ("please enter c: "))
D = (b ** 2) - (4 * a * c)
print 'D = ',D
if D < 0:
  print ("there is no solution, becouse D is < 0")
elif D == 0:
  x = -b / 2 * a
  print ("there is only 1 root becouse D=0")
  print 'x= ',x
else:
  x1 = (-b + math.sqrt(D)) / (2 * a)
  x2 = (-b - math.sqrt(D)) / (2 * a)
  print 'there are two roots:'
  print 'x1= ',x1
  print 'x2= ',x2