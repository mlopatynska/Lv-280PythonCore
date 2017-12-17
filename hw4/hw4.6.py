word = raw_input('Please enter any word, preferably long one :-)\n')
dic = {}
for let in word:
    dic.setdefault(let,0)
    dic[let]=dic[let]+1
print dic


