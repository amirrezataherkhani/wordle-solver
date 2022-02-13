import os
from numpy import character
from collections import defaultdict
import collections
from pyparsing import Word
import time

with open('/usr/share/dict/words') as f:
    i=0
    words_with_5_character = []
    for line in f:
        if len(line.rstrip())==5 and "'" not in line.rstrip():
            words_with_5_character.append(line.rstrip().lower())
while True:
    found_characters = input("green characters with it's indexes seperated with comma (like: m1, n3): ")
    n=2
    found_characters = found_characters.replace(' ','').replace(',','')
    items = [found_characters[i:i+n] for i in range(0, len(found_characters), n)]
    character_with_index = defaultdict(list)
    for item in items:
        character_with_index[item[0]].append(int(item[1]))
    step_one_words = [] # words which contain character given by user
    green_words = []
    for word in words_with_5_character:
        if all([char in word for char in list(character_with_index)]):
            step_one_words.append(word)

    for word in step_one_words:
        result = {}

        for i, c in  enumerate(word):
            result.setdefault(c, []).append(i+1)
        
        i = 0
        for key1 in character_with_index:
            for key2 in result:
                if key1 == key2:
                    if set(character_with_index[key1]).issubset(set(result[key2])):
                            i+=1
        if i==len(character_with_index):
            green_words.append(word)

    good_characters = input("orange characters (like: p,o,l): ")
    good_characters = list(good_characters.replace(',',''))
    orange_words = []
    for word in green_words:
        if all([char in word for char in good_characters]):
            orange_words.append(word)

    removed_characters = input("removed characters (like: g,r,t): ")
    bad_characters = list(removed_characters.replace(',',''))  
    answers = []
    
    for char in bad_characters:
        for word in orange_words[:]:
            if char in word:
                if word in orange_words:
                    index_of_useless_word = orange_words.index(word)
                    orange_words.pop(index_of_useless_word)    
    for word in orange_words:
        print(word)
    atlast = input('solved?')
    if atlast == 'y':
        break
    elif atlast == 'n':
        continue
    else:
        print('wrong input!')
        break