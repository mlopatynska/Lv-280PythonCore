# -*- coding: utf-8 -*-
#Записати в стрічку філософію Пайтона

importthis= str ("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea — let's do more of those!")

#Знайти в заданій стрічці кількість входжень слів (better, never, is)

better = importthis.count("better")
never = importthis.count('never')
i = importthis.count('is')
print 'Кількість слів better = {}, never = {}, is= {}  штук.'.format(better, never, i)

#Вивести весь текст у верхньому регістрі (всі великі літери)

importthis_up=importthis.upper()
print importthis_up

#Замінити всі входження символу i на &

importthis_i=importthis.replace('i','&')
print importthis_i

