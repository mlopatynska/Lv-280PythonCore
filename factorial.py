def factorial(g):
        f=1
        for x in range (1,g+1):
            f=f*x
        return(f)
n=int(input())
m=int(input())
tot=0
tot=(factorial(n) + factorial(m)) / factorial(n + m)
print(tot)  