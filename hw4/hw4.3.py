N=input('Please enter any number except 0\n')
fib1 = [0, 1]
for num in range(2, N + 1):
    fib1.append(fib1[num - 1] + fib1[num - 2])
print (fib1)
