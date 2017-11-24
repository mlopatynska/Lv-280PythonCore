fib=int(raw_input('Please enter fibonachi number:'))
if fib!=1:
    x=range(fib+1)
    x[0]=0
    x[1]=1
    sum=1
    rez=[]
    for i in range(fib-2):
     sum+=1
     x[sum]=x[sum-1]+x[sum-2]
     rez.append(x[sum])   
    print 'The first {} fibonachi numbers is:{}'.format(fib,[0,1]+rez) 
else:
    print 'The first fibonachi number is 0 !' 