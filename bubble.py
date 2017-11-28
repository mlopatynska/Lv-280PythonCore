a=[100,10,90,50,30,80,40,60,20,70,0]
b=[5,4,9,40,34,85,45,65,25,74,3]

def my_sort(n):
    for i in range (len(n)-1,0,-1): 
        for x in range(i): 
            if n[x] < n[x+1]: 
                n[x] , n[x+1] = n[x+1] ,n[x] 
    return n
print( my_sort(a), my_sort(b))







