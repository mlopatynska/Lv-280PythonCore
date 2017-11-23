n = int(input("please enter a number: "))
suma = 0
while n > 0:
 last = (n % 10)*(n % 10)* (n % 10)
 suma += last
 n //= 10
print 'sum is: ', suma

