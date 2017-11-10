num = 1357672549
mystr = str(num)
print mystr
sortedlist = sorted(mystr)
print sortedlist
newstr = ''.join(sortedlist)
newint = int(newstr)
print newint
print type(newint)


number = 1357672549
my_sorted_number = int(''.join(sorted(str(number))))
print my_sorted_number