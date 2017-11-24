integer=int(raw_input('Please enter your integer:'))
counter=integer
while counter > 1:
    counter=counter-1 
    if counter==1:
     print 'Your integer is simple.'
     break
    if integer%counter==0:
     print 'Your integer is UNSIMPLE.'
     break 