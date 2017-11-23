#smallest number
#list=[2,4,6,8,1,10]
list = []
print ('Please enter up to 7 numbers in a list.\n')
while len(list)<7:
    list.append(input())
small = list[0]
for i in list:
    if small<i:
        small=small
    else:
        small=i
print ('The smallest number in this list is {}'.format(small))


#biggest number
#list=[2,4,6,8,1,10]
list = []
print ('Please enter up to 7 numbers in a list.\n')
while len(list)<7:
    list.append(input())
small=0
for i in list:
    if i>small:
        small=i
    else:
        small=small
print ('The biggest number in this list is {}'.format(small))