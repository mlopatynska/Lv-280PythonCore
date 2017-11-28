def words():
    word_1 = raw_input("enter the main word: ")
    word_2 = raw_input("enter the 1 word: ")
    word_3 = raw_input("enter the 2 word: ")
    word_4 = raw_input("enter the 3 word: ")
    word_5 = raw_input("enter the 4 word: ")
    word_6 = raw_input("enter the 4 word: ")
    if sorted(word_2.lower()) == sorted (word_1. lower()):
        print 'with permutatiom of letters in word ', word_2, 'you can make a word ', word_1
    elif sorted(word_3.lower()) == sorted (word_1. lower()):
        print 'with permutatiom of letters in word ', word_3, 'you can make a word ', word_1
    elif sorted(word_4.lower()) == sorted (word_1. lower()):
        print 'with permutatiom of letters in word ', word_4, 'you can make a word ', word_1
    elif sorted(word_5.lower()) == sorted (word_1. lower()):
        print 'with permutatiom of letters in word ', word_5, 'you can make a word ', word_1
    elif sorted(word_6.lower()) == sorted(word_1.lower()):
        print 'with permutatiom of letters in word ', word_6, 'you can make a word ', word_1
    else:
        print 'there are not any similar words'

words()