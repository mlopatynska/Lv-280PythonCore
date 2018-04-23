#variant 1, iteration, correct

def facto(n):
    factor = 1
    for i in range(1,n+1):
        factor *=i
    return factor
print (facto(0))


#variant 2, recursion, correct
def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n-1)
print (facto(10))


m = input('please enter any 2 positive numbers:\n')
n = input()
def facto_multi(m, n):  # this is the functio which defines final result F(nm)
        start = 1
        if m == 0 or 1:
            factom = float(1)
        else:
            for num in range (2,m+1):
                factom=float(start*num)
                start=factom
        start = 1
        if n == 0 or 1:
            facton = float(1)
        else:
            for num in range(2, n+1):
                facton = float(start*num)
                start=facton
        facto_multi=(factom * facton)/(n+m)
        print facto_multi
facto_multi (m,n)


