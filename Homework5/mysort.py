my_list1 = input('Enter list first time\n')
my_list2 = list(input('Enter list first time'))

def my_sort(lis):
    n = 1
    while n < len(lis):
        for i in range(1,len(lis)):
            if lis[i-1] < lis[i]:
                lis[i-1],lis[i] = lis[i],lis[i-1]
    n += 1
    print(lis)
    return(lis)

my_sort(my_list1)