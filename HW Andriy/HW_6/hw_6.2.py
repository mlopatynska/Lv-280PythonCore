def factorial(number):
    fact_product = 1
    for i in range (1, number+1):
        fact_product *= i
    return fact_product

def formula(m, n):
    return float((factorial(n)*factorial(m))/factorial(n + m))

print formula(1,2)