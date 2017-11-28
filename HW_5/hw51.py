import random
import math
def calculate_the_equation(x,y,z):
    list_a=[]
    for i in range(30):
        x=random.uniform(1,5)
        list_a.append(x)
    list_b=[]
    for i in range(30):
        x=random.uniform(1,5)
        list_b.append(x)  
    list_c=[]
    for i in range(30):
        x=random.uniform(1,5)
        list_c.append(x)
 
    val1=0
    for i in range(30):
        val1+=list_a[0+i]*math.pow(x,30-i)

    val2=0
    for i in range(30):
        val2+=list_b[0+i]*math.pow(y,30-i)

    val3=0
    for i in range(30):
        val3+=list_c[0+i]*math.pow((x+z),30-i)
  
    return (math.pow(val1,2)-val2)/val3
#print calculate_the_equation(1,2,3) 