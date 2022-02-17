#!/usr/bin/env python

import sys
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from collections import Counter

#take in input text, line for line
input_text = [line.strip() for line in sys.stdin]

#convert list to a string
text = str(input_text)

#tokenize input text
tokens = word_tokenize(text)

#convert all tokens to lowercase
tokens_lower = [token.lower() for token in tokens]

#count all tokens
token_count = Counter(tokens_lower)

#sort by frequency and print each token with it's count
for token, value in token_count.most_common():
    print(token, value)