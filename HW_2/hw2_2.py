numb= 1825
numb_became_str = str(numb)
result=1
 
for i in numb_became_str:
    f=int(i)
    result=result*f
print 'product of numbers is:' , result
# reverse
print 'reverse of numbers is:' , numb_became_str[::-1]
#sorted
print "sorted numbers       :" , ''.join(sorted(numb_became_str))
#changing variables
x=22 
y=7
x,y=y,x
print 'result of changing variables is :', x ,'&', y
