def factorial(n):
    if n == 0:
        return 1

        f = 1
        for i in range(1, n + 1):
            f *= i
        return f
n = 5
m = 6
s = m + n
print (n, (factorial(n) * factorial(m)) / factorial(s))