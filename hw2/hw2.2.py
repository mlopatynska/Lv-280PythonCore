num='2345'

print (num)

sum=int(num[0])+int(num[1])+int(num[2])+int(num[3])

print (sum)

rev=list(reversed(num))

print(rev)

print(str(rev[0] + rev[1]+rev[2]+rev[3]))

numsor=(list(num))
numsor.sort(reverse=True)
print(numsor)

#task 3, reassignment of 2 variables
v1,v2=234,345
print v1, v2
v1,v2=v2,v1
print v1, v2