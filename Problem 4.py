def palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

def factors(n):
    for x in range(100, 1000):
        if n % x == 0:
            if len(str(n//x)) == 3:
                print(x, n//x)
                return True
    return False

n = 998001

while True:
    if palindrome(n):
        if factors(n):
            print(n)
            break
    print(n)
    n -= 1