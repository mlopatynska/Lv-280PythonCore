from math import sqrt

print "To check if equation ax2+bx+c=0 has any square roots please enter:"
a = input("a = ")
b = input("b = ")
c = input("c = ")

if b**2-4*a*c < 0:
    print "There are no square roots for this equation"
elif b**2-4*a*c == 0:
    print "The square root for the equation is {}".format(-b / (2 * a))
else:
    print "The square roots for the equation are {} and {}"\
        .format((-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a))
