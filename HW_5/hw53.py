def perestanovka(x,y):
    dict_y={i:y.count(i) for i in y}
    list_x=x.split()
    count=-1
    rezult=[]
    for word in list_x:
        count+=1 
        dict_x={i:word.count(i) for i in word}
        if dict_x==dict_y:
		    rezult.append(list_x[count])
    return ','.join(rezult)
#print perestanovka('tysda stady program','datsy')