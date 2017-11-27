text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one -- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

begin_with = raw_input("Please input first letters of the words, you want to find in Python Philosophy\n")
text_list = text.split()
found_words = {}

for i in range(len(text_list)):
    if begin_with == text_list[i][0:len(begin_with)]:
        found_words[text_list[i].replace(".", "")] = ""

print "The words in Python Philosophy that begin with \'{}\' are {}"\
    .format(begin_with, str(found_words.keys())).replace("[", "").replace("]", "")