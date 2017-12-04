num = input("Enter number please:")
fib_1=0
fib_2=1

def fib(count, n1,n2):
    if count<=0:
        return n1
    else:
        print n1
        return fib(count-1,n2, n1+n2)

fib(num, fib_1,fib_2)