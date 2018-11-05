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
def check(s, q, qc):
    if s[q] == s[qc]:
        return True
    else:
        return False

def closest(s, queries):
    # Write your code here
    a = []
    for query in queries:
        i = query
        j = query
        l = len(s)
        flag = 0
        if queries.co
        while (i != 0) or (j != (l-1)):
            if i != 0:
                i -= 1
                flag = check(s,i,query)
            if flag:
                break
            if j != (l-1):
                j += 1
                flag = check(s,j,query)
            if flag:
                break
        if flag != 1:
            a.append(-1)
        else :
            if (s[i] == s[query]) and (i != query) :
                a.append(i)
            elif (s[j] == s[query]) and (j != query):
                a.append(j)
    return a

if __name__ == '__main__':
