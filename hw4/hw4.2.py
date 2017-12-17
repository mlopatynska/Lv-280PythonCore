n=input('Please type any positive number\n')
for num in range(2,n):
    if n%num==0: # prime numbers can be divided without remainder only by 1 and itself, if remainder==0 - not prime
        print ('Your number is not a prime number!')
        break
    else:
        print ('Your number is prime!')
        break
