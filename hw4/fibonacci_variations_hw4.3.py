#Fibonacci numbers
#variant 1
N=input('Please enter any number except 0\n')
fib1 = [0, 1]
for num in range(2, N + 1): #here we state that 1-st number of Fibonacci is 0, second - 1, so n is always >2
    fib1.append(fib1[num - 1] + fib1[num - 2]) #n=(n-1)+(n-2), n>2
print (fib1)


#variant 2
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n=input('Please enter any positive number\n')
fib=[0,1]
for i in range(n-1): #here we does not state that n must be more then 2
  fib.append(fib[i]+fib[i+1])
print fib


# returns Fibonacci sequence
def fibo(n):
   seq = [1,1]
   if n == 1:
       return [1]
   elif n == 2:
        return seq
   else:
        for num in range(2, n): 
            seq.append(seq[num - 1] + seq[num - 2])
        return seq
        
print(fibo(4))
