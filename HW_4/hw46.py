new_word = raw_input("Please enter a word: ")
dict={i:new_word.count(i) for i in new_word}
print "The word {} is divided into : {}".format(new_word,dict)