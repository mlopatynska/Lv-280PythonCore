a = input("enter 4-character digit: ")
a_tuple = tuple(str(a))
a_list = list(a_tuple)
a_list.reverse()
a_rev = int(''.join(a_list))
print "The result of reversion of typed digit is: ",  a_rev