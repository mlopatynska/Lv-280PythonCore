list1 = [1, 2, 6, 67, 43, 2]
list2=[23,45,2,123,546,89,12]
def mysort(x):
    for passnum in range(len(x)-1,0,-1):
    	for i in range(passnum):
            if x[i]<x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    print x
mysort(list1)
mysort(list2)