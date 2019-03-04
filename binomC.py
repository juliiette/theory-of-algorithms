"""

Write the function C (m, n) of the calculation of
binomial coefficients according to the given
formula

"""

def C(m, n):
    if m == 0 or m == n:
        return 1
    else:
        return C(m, n - 1) + C(m - 1, n - 1)


m = int(input('Type your m:  '))
n = int(input('Type your n:  '))
print(C(m, n))

