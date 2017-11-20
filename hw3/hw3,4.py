import math
s1=float(input ('Type the length of the first side of the triangle in centimeters:\n'))
s2=float(input('Second side now:\n'))
s3=float(input('Third side:\n'))
# Hint: any side of the triangle cannot be longer then the sum of 2 other sides!
if s1 >= (s2+s3) or s2 >= (s1+s3) or s3 >= (s1+s2):
    print ('You cannot build a triangle with such side lengths! Please try again')
else:
    print ('The perimeter of our triangle is {0}+{1}+{2}='.format(s1,s2,s3) + str(s1+s2+s3) + ' centimeters')
    # the semiperimeter of triangle = perimeter/2
    P=(s1+s2+s3)/2 # ask how to make it a float with numbers after point
    # area of triangle by Heron's formula: S=square root of P(P-a)(P-b)(P-c)
    S=math.sqrt(P*(P-s1)*(P-s2)*(P-s3))
    print ('The area of our triangle is {0}'.format(S) + ' centimeters')