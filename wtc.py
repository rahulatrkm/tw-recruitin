#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'closest' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def closest(s, queries):
    # Write your code here
    a = []
    #print(s)
    #print(queries)

    for query in queries:
        c = s.count(s[query])
        #print(c)
        #print(a)
        if c == 1:
            a.append(-1)
        elif (query == 0):
            i = 1
            while (s[query] != s[i]):
                i +=1
            a.append(i)
        elif (query == (len(s)-1)):
            i = (len(s)-2)
            while (s[query] != s[i]):
                i -= 1
            a.append(i)
        else:
            if query > 0:
                i = query - 1
            else :
                i = query
            if query < (len(s)-1):
                j = query + 1
            else :
                j = query
            while ((s[i] != s[query]) and (s[j] != s[query])):
                if i > 0:
                    i -= 1
                if j < (len(s)-1):
                    j += 1
                if (i == 0) and (j == (len(s)-1)):
                    break
            print(i, s[i])
            print(j, s[j])
            if ((s[i] == s[query]) and (i != query)):
                a.append(i)
            elif ((s[j] == s[query]) and (j != query)):
                a.append(j)
    return a


if __name__ == '__main__':
