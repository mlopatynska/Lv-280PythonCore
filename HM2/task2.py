# -*- coding: utf-8 -*-
#Задано чотирицифрове натуральне число

#Знайти добуток цифр цього числа
mynum = raw_input("Please, input a four-digit number:")
mynum = list(mynum)
mynum = map(int,mynum) #map применяет функцию ко всем элементам списка map(function_to_apply, list_of_inputs)
print 'number to multiply=', mynum [0] * mynum[1] * mynum[2] * mynum[3] #знаходимо добуток елементів списка

#Записати число в реверсному порядку
mynum = map(str,mynum)
mynum.reverse()
rev_list = "".join(mynum)
print 'reverse number=', rev_list

#Посортувати цифри, що входять в дане число
sorted_num =int("".join(sorted(mynum)))
print 'sorted number=', sorted_num