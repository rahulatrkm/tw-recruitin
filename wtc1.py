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
    # hash map for string
    sd = dict()
    # index for insertion in list
    ind = dict()
    i = 0
    j = len(s)-1
    while (i<=j):
        if s[i] in sd:
            sd[s[i]].insert(ind[s[i]],i)
            ind[s[i]] += 1
        else:
            sd[s[i]] = [i]
            ind[s[i]] = 1
        if i != j:
            if s[j] in sd:
                sd[s[j]].insert(ind[s[j]],j)
            else:
                sd[s[j]] = [j]
                ind[s[j]] = 0
        print(ind)
        i += 1
        j -= 1
    print(sd)

    a = []
    for query in queries:
        temp = sd[s[query]]
        t1 = temp.index(query)
        if len(temp) == 1:
            a.append(-1)
        else:
            if t1 == 0:
                a.append(temp[1])
            elif t1 == (len(temp)-1):
                a.append(temp[t1-1])
            else:
                if abs(temp[t1-1] - query) <= abs(temp[t1+1] - query):
                    a.append(temp[t1-1])
                else:
                    a.append(temp[t1+1])

    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = closest(s, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
