'''def factorial(x):
    result = 1
    for i in xrange(2, x + 1):
        result *= i
    return result

print factorial(10)'''




import math
n = input('enter n: ')
m = input('enter m: ')
f = math.factorial
print'factorial of n is: ',(f(n))
print 'factorial of m is: ',(f(m))
print 'the sum of f(n) and f(m) is: ', f(n) + f(m)
print 'factorial of n+m is: ', f(n+m)
F = float((f(n)+f(m)) / f(n+m))
print 'F = ',F
