import math
import os
import random
import re
import sys

# Complete the lagDuration function below.
def lagDuration(h1, m1, h2, m2, k):
    return(((h1+k)*60+m1) -(h2*60+m2) )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        h1M1H2M2 = input().split()

        h1 = int(h1M1H2M2[0])

        m1 = int(h1M1H2M2[1])

        h2 = int(h1M1H2M2[2])

        m2 = int(h1M1H2M2[3])

        k = int(input())

        result = lagDuration(h1, m1, h2, m2, k)

        fptr.write(str(result) + '\n')

    fptr.close()
