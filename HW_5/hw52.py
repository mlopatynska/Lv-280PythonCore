def F(m,n):
    fact_m=1
    i=0
    for rrr in range(m):
        i+=1
        fact_m=fact_m*i
    fact_n=1
    i=0
    for rrr in range(n):
        i+=1
        fact_n=fact_n*i
    return fact_n * fact_m/(fact_n+fact_m)
#print F(3,3)	