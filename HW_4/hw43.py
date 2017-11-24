my_int=(raw_input('Please enter an integer: '))
y=[]
for i in my_int:
    i=int(i)
    y.append(pow(i,3))
print "The sum of the cubes of the numbers of a given natural number is {} !".format(sum(y))