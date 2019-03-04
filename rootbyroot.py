"""

Calculate, using recursion, an expression

"""

import math


def recursion(n, m, x):
    if x == 1:
        return math.pow(n + m, .5)
    else:
        return math.pow(n + m * recursion(n + 1, m + 1, x - 1), .5)


x = int(input('Type the deep of expression:  '))
n = int(input('Type your n:  '))
m = int(input('Type your m:  '))
print(recursion(n, m, x))
