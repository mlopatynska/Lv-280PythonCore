#!/usr/bin/python
# -*- coding: utf-8 -*-

ukr_word = raw_input("Write a word in ukrainian\n").decode("utf-8")

word_list = list(ukr_word)

for symbol_number in range(0, len(word_list)):
    if word_list[symbol_number] == u"А":
        word_list[symbol_number] = "A"
    elif word_list[symbol_number] == u"а":
        word_list[symbol_number] = "a"
    elif word_list[symbol_number] == u"Б":
        word_list[symbol_number] = "B"
    elif word_list[symbol_number] == u"б":
        word_list[symbol_number] = "b"
    elif word_list[symbol_number] == u"В":
        word_list[symbol_number] = "V"
    elif word_list[symbol_number] == u"в":
        word_list[symbol_number] = "v"
    elif word_list[symbol_number] == u"Г":
        word_list[symbol_number] = "H"
    elif word_list[symbol_number] == u"г":
        word_list[symbol_number] = "h"
    elif word_list[symbol_number] == u"Ґ":
        word_list[symbol_number] = "G"
    elif word_list[symbol_number] == u"ґ":
        word_list[symbol_number] = "g"
    elif word_list[symbol_number] == u"Д":
        word_list[symbol_number] = "D"
    elif word_list[symbol_number] == u"д":
        word_list[symbol_number] = "d"
    elif word_list[symbol_number] == u"Е":
        word_list[symbol_number] = "E"
    elif word_list[symbol_number] == u"е":
        word_list[symbol_number] = "e"
    elif word_list[symbol_number] == u"Є":
        word_list[symbol_number] = "Ye"
    elif word_list[symbol_number] == u"є":
        word_list[symbol_number] = "ie"
    elif word_list[symbol_number] == u"Ж":
        word_list[symbol_number] = "Zh"
    elif word_list[symbol_number] == u"ж":
        word_list[symbol_number] = "zh"
    elif word_list[symbol_number] == u"З":
        word_list[symbol_number] = "Z"
    elif word_list[symbol_number] == u"з":
        word_list[symbol_number] = "z"
    elif word_list[symbol_number] == u"И":
        word_list[symbol_number] = "Y"
    elif word_list[symbol_number] == u"и":
        word_list[symbol_number] = "y"
    elif word_list[symbol_number] == u"І":
        word_list[symbol_number] = "I"
    elif word_list[symbol_number] == u"і":
        word_list[symbol_number] = "i"
    elif word_list[symbol_number] == u"Ї":
        word_list[symbol_number] = "Yi"
    elif word_list[symbol_number] == u"ї":
        word_list[symbol_number] = "i"
    elif word_list[symbol_number] == u"Й":
        word_list[symbol_number] = "Y"
    elif word_list[symbol_number] == u"й":
        word_list[symbol_number] = "y"
    elif word_list[symbol_number] == u"К":
        word_list[symbol_number] = "K"
    elif word_list[symbol_number] == u"к":
        word_list[symbol_number] = "k"
    elif word_list[symbol_number] == u"Л":
        word_list[symbol_number] = "L"
    elif word_list[symbol_number] == u"л":
        word_list[symbol_number] = "l"
    elif word_list[symbol_number] == u"М":
        word_list[symbol_number] = "M"
    elif word_list[symbol_number] == u"м":
        word_list[symbol_number] = "m"
    elif word_list[symbol_number] == u"Н":
        word_list[symbol_number] = "n"
    elif word_list[symbol_number] == u"н":
        word_list[symbol_number] = "n"
    elif word_list[symbol_number] == u"О":
        word_list[symbol_number] = "O"
    elif word_list[symbol_number] == u"о":
        word_list[symbol_number] = "o"
    elif word_list[symbol_number] == u"П":
        word_list[symbol_number] = "P"
    elif word_list[symbol_number] == u"п":
        word_list[symbol_number] = "p"
    elif word_list[symbol_number] == u"Р":
        word_list[symbol_number] = "R"
    elif word_list[symbol_number] == u"р":
        word_list[symbol_number] = "r"
    elif word_list[symbol_number] == u"С":
        word_list[symbol_number] = "S"
    elif word_list[symbol_number] == u"с":
        word_list[symbol_number] = "s"
    elif word_list[symbol_number] == u"Т":
        word_list[symbol_number] = "T"
    elif word_list[symbol_number] == u"т":
        word_list[symbol_number] = "t"
    elif word_list[symbol_number] == u"У":
        word_list[symbol_number] = "U"
    elif word_list[symbol_number] == u"у":
        word_list[symbol_number] = "u"
    elif word_list[symbol_number] == u"Ф":
        word_list[symbol_number] = "F"
    elif word_list[symbol_number] == u"ф":
        word_list[symbol_number] = "f"
    elif word_list[symbol_number] == u"Х":
        word_list[symbol_number] = "Kh"
    elif word_list[symbol_number] == u"х":
        word_list[symbol_number] = "kh"
    elif word_list[symbol_number] == u"Ц":
        word_list[symbol_number] = "Ts"
    elif word_list[symbol_number] == u"ц":
        word_list[symbol_number] = "ts"
    elif word_list[symbol_number] == u"Ч":
        word_list[symbol_number] = "Ch"
    elif word_list[symbol_number] == u"ч":
        word_list[symbol_number] = "ch"
    elif word_list[symbol_number] == u"Ш":
        word_list[symbol_number] = "Sh"
    elif word_list[symbol_number] == u"ш":
        word_list[symbol_number] = "sh"
    elif word_list[symbol_number] == u"Щ":
        word_list[symbol_number] = "Shch"
    elif word_list[symbol_number] == u"щ":
        word_list[symbol_number] = "shch"
    elif word_list[symbol_number] == u"Ю":
        word_list[symbol_number] = "Yu"
    elif word_list[symbol_number] == u"ю":
        word_list[symbol_number] = "yu"
    elif word_list[symbol_number] == u"Я":
        word_list[symbol_number] = "Ya"
    elif word_list[symbol_number] == u"я":
        word_list[symbol_number] = "ia"
    elif word_list[symbol_number] == u"Ь":
        word_list[symbol_number] = ""
    elif word_list[symbol_number] == u"ь":
        word_list[symbol_number] = ""
    elif word_list[symbol_number] == u"'":
        word_list[symbol_number] = ""

print ''.join(word_list)