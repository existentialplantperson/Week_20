#!/usr/bin/env python

import sys

#take all the words from mapper and count the individual words
current_word = None
current_count = 0
word = None

#take output from mapper.py file and process
for line in sys.stdin:
    line = line.strip()

    word, count = line.split("\t", 1)

    #aggregate counts together
    #try except here is a good idea
    count = int(count)

    #sorted values from comman line passed in
    #if we have multiples, increment counter for that word

## terminal: echo 'the quick brown fox jumped over the lazy dog'|./mapper.py|sort

    if current_word == word:
        current_count += count
    else:
        #handles the None instantiation scenario
        if current_word:
            print(current_word + "\t" + str(current_count))

        #reset for next loop
        current_count = count 
        current_word = word

#not iterating through last word, need to make an edge case
if current_word == word:
    print(current_word + "\t" + str(current_count))       

## terminal: echo 'the quick brown fox jumped over the lazy dog'|./mapper.py|sort|./reducer.py

## ANOTHER EXAMPLE
# concatenate (cat) .txt file map, sort, reduce
## terminal: cat ../cats_txt.txt|./mapper.py|sort|./reducer.py