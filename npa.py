#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimalOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY words as parameter.
#

def minimalOperations(words):
    # Write your code here
    c = []
    for word in words:
        word = list(word)
        tc = 0
        for i,j in enumerate(word):
            if i > 0:
                if word[i-1] == j:
                    tc += 1
                    word[i] = '0'
        c.append(tc)
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = minimalOperations(words)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
