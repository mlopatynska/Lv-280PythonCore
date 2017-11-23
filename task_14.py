a = int(input("please enter a number: "))
prime = True
i = 2
while i <= a-1:
 if a % i == 0:
    prime = False
 i = i + 1
if prime:
 print 'number', a, 'is prime'
else:
 print 'number', a, 'is not prime'