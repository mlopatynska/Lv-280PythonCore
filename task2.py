a = raw_input("a=")
b = raw_input("b=")
if b=='0':
    print 'it is bad idea'
    exit()
a = int(a)
b = int(b)
sum = a+b
min = a-b
mn = a*b
div = a/b
print 'a+b=', sum
print 'a-b=', min
print 'a*b=', mn
print 'a/b=', div