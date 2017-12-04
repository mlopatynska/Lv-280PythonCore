#!/usr/bin/python
# -*- coding: utf8 -*-
mystr=raw_input("Enter some string please:")
mylist={}
for i in range(len(mystr)):
    #if mystr[i] not in mylist:
    mylist[mystr[i]]=mystr.count(mystr[i])


print mylist