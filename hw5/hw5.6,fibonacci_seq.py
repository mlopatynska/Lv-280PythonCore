# F(1) = F(2) = 1; F(n) = F(n - 1) + F(n - 2). Recursion - allowing a function to call itself within the program text
# recursive function, slower one
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2) #function calls itself again
print fib(9)
