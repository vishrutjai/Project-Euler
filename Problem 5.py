def multiples(n):
    for x in range(1, 21):
        if n % x != 0:
            return False
    return True


a = 10
while True:
    if multiples(a):
        print(a)
        break
    a += 1
