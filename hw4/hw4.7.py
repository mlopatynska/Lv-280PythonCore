#variant 1:
st='''Peter Piper picked a peck of pickled peppers.
A peck of pickled peppers Peter Piper picked.
If Peter Piper picked a peck of pickled peppers,
Where's the peck of pickled peppers Peter Piper picked?
   '''
list=st.split()
dic={}
for i in list:
  comp=i[0:3].lower()
  dic.setdefault(comp,0)
  dic[comp]=dic[comp]+1
  #print (dic)
for k,v in dic.items():
  if v>1:
    print (k)
    print ('{} words start with {}:'.format(v,k))
    
  
 
#variant 2:
st='''Peter Piper picked a peck of pickled peppers.
A peck of pickled peppers Peter Piper picked.
If Peter Piper picked a peck of pickled peppers,
Where's the peck of pickled peppers Peter Piper picked?
   '''
print (st)
letters=raw_input("You see a string. Please type any 3-letter beginning of any word here, i. e. 'pet'\n")
list=st.split()
#print (list)
for i in list:
  if letters in st:
    if i[0:3].lower() == letters:
      print(i)
  else:
    print ('No such beginning of words in this text!')
    break
  
    
