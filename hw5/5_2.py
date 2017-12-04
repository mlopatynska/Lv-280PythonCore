num_1 = input("Enter first number please:")
num_2 = input("Enter second number please:")

def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return (x * factorial(x - 1))

print (float(factorial(num_1)*factorial(num_2))/factorial(num_1+num_2))
