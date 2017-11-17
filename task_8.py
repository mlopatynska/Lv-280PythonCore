a = input("enter 4-character digit: ")
a_tuple = tuple(str(a))
a_list = list(a_tuple)
a_sort = int(''.join(sorted(str(a))))
print "the sorted digit that you have just typed is: ", a_sort