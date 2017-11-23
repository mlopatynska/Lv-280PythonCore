mystr=raw_input("Enter some string please:")
mylist={}
for i in range(len(mystr)):
    if mystr[i] not in mylist:
        mylist[mystr[i]].append(mystr.count(mystr[i]))


print mylist #mystr[i]+":"+str(mystr.count(mystr[i]))