x=[3,7,8,2,9,5,5,4,1]

Min=x[0]
for i in range(1,len(x)):
    if Min>int(x[i]):
        Min=int(x[i])

print ('{} min = {}').format(x,Min)

print"------------------------------------"


word='dictionary'

dword={word[x]:word.count(word[x])for x in range(len(word))}

print dword
