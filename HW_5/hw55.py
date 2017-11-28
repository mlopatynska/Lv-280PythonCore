def sort(x):
    for value in range(len(x)-1,0,-1):
    	for i in range(value):
            if x[i]>x[i+1]:
                x[i],x[i+1] = x[i+1],x[i]
    return x				
x=[22,4,454,5,76576,9]	
y=[4,9,65,32,8]			
print sort(x)	
print sort(y)			