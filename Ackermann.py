def ackermann(n, m):
    if n == 0:
        return m+1
    if n != 0 and m == 0:
        return ackermann(n-1, m)
    if n > 0 and m >= 0:
        return ackermann(n-1, ackermann(n, m-1))
    else:
        return False


to_do = input('Calculate?  ')
while to_do != 'no':
    n = int(input('Enter your n:  '))
    while n < 0:
        print('n must be +')
        n = int(input('Enter your n:  '))
    m = int(input('Enter your m:  '))
    while m < 0:
        print('m must be +')
        m = int(input('Enter your m:  '))
    result = ackermann(n, m)
    print(result)
    to_do = input('Calculate?  ')
