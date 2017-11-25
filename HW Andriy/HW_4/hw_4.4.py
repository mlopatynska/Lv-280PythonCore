from math import sqrt

print "To calculate perimeter and area of a triangle please enter the lenghs of it's sides:"
side1 = input("Side 1 = ")
side2 = input("Side 2 = ")
side3 = input("Side 3 = ")

print ""

if side1 >= side2 + side3 or side2 >= side1 + side3 or side3 >= side2 + side1:
    print "There can't be a triangle with such sides"
else:
    perimeter = side1 + side2 + side3
    area = sqrt((perimeter / 2) * (perimeter / 2 - side1) * (perimeter / 2 - side2) * (perimeter / 2 - side3))
    print "The perimeter of this triangle = {} and the area = {}".format(perimeter, area)
