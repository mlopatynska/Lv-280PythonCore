num=input('Please enter any one-digit number, from 1 to 9\n')
sum=(range(1000,10000))
for n in sum:
    s=str(n)
    su=0
    for i in s:
        su=su+int(i)
    if su==num:
        print ('The sum of digits in {} equals {}'.format (n,num))



num=input('Please enter any one-digit number, from 1 to 9\n')
sum=(range(1000,10000))
list_of_num = []
for n in sum:
    s=str(n)
    su=0
    for i in s:
        su=su+int(i)
    if su==num:
        list_of_num.append(s)
print ('The sum of digits in {} equals {}'.format (list_of_num,num))