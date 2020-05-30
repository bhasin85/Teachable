#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k, n):
    for i in range(n):
        c_ord = ord(s[i])
        if 65 <= c_ord <= 90:
            c_ord += k
            if c_ord > 90:
                c_ord = c_ord - 25
            s[i] = chr(c_ord)
        elif 97 <= c_ord <= 122:
            c_ord += k
            if c_ord > 122:
                c_ord = c_ord - 25
            s[i] = chr(c_ord)

    return "".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(list(s), k, n)

    fptr.write(result + '\n')

    fptr.close()
