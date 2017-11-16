num=int(raw_input("Enter four digit number please:"))
print ("Reverse                        "+str(num)[::-1])

mystr=list(str(num))
mystr.sort()
mystr=''.join(mystr)
print("Sorted                         "+mystr)

multpl=1

while num > 0:
    if num % 10 != 0:
        multpl = multpl * (num % 10)
    num = num // 10

print("Multiplication of digits equal: "+str(multpl))