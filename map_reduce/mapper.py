#!/usr/bin/env python
#shebang line to tell terminal where Python can be found

import sys #system variables

#goal - run program and pass a file or a sentence into it

#stdin = standard input
for line in sys.stdin:
    
    #remove white spaces at beginning and end of line
    line = line.strip()

    #split each line up
    words = line.split()

    # process each words and assign a value of 1 to each word
    for word in words:
        print(word + "\t1")



#mapper - breaking up words into units