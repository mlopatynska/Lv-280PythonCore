for x in range(a,b,h):
    y=2*x/((1-x)**3) #(x-1)*exp(x)+1
    s=0
    k=1
    p=1
    while p>E:
        k+=1
        s+=(k*(k+1))*x**k #(1/factorial(k)*(k+2))*x**(k+2)
        p=fabs((s-y)/y)*100
        print str(k)+' '+str(s)+' '+str(p)


    print("{}       {}      {}      {}".format(x,s,y,p))