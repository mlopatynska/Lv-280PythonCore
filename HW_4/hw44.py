text=raw_input('input text:')
symbols=raw_input('input symbols:')
list_text=text.split(' ')
len_sym=len(symbols)
f_list=[]
for i in list_text:
    if symbols in i[:len_sym]:
        f_list.append(i)
print "This is your new text: {}.".format(','.join(f_list))