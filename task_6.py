a = input("enter 4-character digit: ")
a_tuple = tuple(str(a))
action = eval('*'.join(a_tuple))
print ("The result of multiply is=: ", action)

