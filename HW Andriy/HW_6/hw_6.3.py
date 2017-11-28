def perestanovka(x, *y):
    dictionary_1 = {}
    selected_y = []
    not_selected_y = []
    for letters_1 in x:
        dictionary_1[letters_1] = x.count(letters_1)
    for word_in_y in y:
        select_word = True
        for letters_2 in word_in_y:
            select_word *= dictionary_1[letters_2] >= word_in_y.count(letters_2)
        if select_word == True:
            selected_y.append(word_in_y)
        else:
            not_selected_y.append(word_in_y)

    print "From changing letters order in word '{}' you can make such words: {}; but not {}"\
    .format(x, str(selected_y).replace("[", "").replace("]", ""), str(not_selected_y).replace("[", "").replace("]", ""))


perestanovka("ababahalamaha", "baba", "bahama", "mama", "lama", "hahaha")