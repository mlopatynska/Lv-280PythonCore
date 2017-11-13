number = input("Please input 4-digit number\n")

my_tuple = tuple(str(number))
multiply = eval('*'.join(my_tuple))
print '\n', 'Each number multiplied =', multiply

my_list = list(my_tuple)
my_list.reverse()
revedred_number = int(''.join(my_list))
print '\n', 'Reversed number =',  revedred_number

sorted_list = int(''.join(sorted(str(number))))
print '\n', 'Sorted number =', sorted_list
