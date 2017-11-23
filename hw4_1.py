x=input("Enter digit x = ")

def suma(digit):
    d=str(digit)
    s=int(d[0])+int(d[1])+int(d[2])+int(d[3])
    return s

'''if not (x<=0 or x>36):
    i=1000
    while i<=9999:
        if suma(i)==x:
            print "{}".format(i)
            i+=1
        else: i+=1
else: print "Not"'''

if not (x<=0 or x>36):
    for i in range(1000,10000):
        if suma(i)==x:
            print "{}".format(i)
else: print "Not"
