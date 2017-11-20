import cmath
a = input('Please enter 3 integers, one by one: \n')
b = input()
c = input()

#solution for any quadratic euqation is x = (-b +/-square root of (b2 - 4ac))/2a

# finding discriminant (according to the algorithm of solving quadratic equations:
# https://www.programiz.com/python-programming/examples/quadratic-roots)
# D=b**2-4ac
D=b**2 - 4*a*c
print ('Discriminant of the equation ax**2 + bx + c = 0 is {0}'.format (D))

if a or b or c == 0:
    print ('Please restart the program and make sure all of your numbers are not equal to 0')
else:
    sol1 = (-b - cmath.sqrt(D))/(2*a)
    sol2 = (-b + cmath.sqrt(D))/(2*a)
    print ('The solution for our equation is {0} and {1}'.format (sol1,sol2))





