k=int(raw_input("Input integer between 1 and 365:"))

if k%7== 1:
    n= 'monday'
if k%7== 2:
    n= 'tuesday' 
if k%7== 3:
    n= 'wednesday'
if k%7== 4:
    n= 'thursday'
if k%7== 5:
    n= 'friday'
if k%7== 6:
    n= 'saturday'
if k%7== 0:
    n= 'sunday'
print'{} integer got {}.'.format(k,n)