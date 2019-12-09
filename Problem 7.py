def prime(n):
    for x in range(2, int(n**(1/2))+1):
        if n % x == 0:
            return False
    return True

count = 0
num = 2
while count != 10001:
    if prime(num):
        count += 1
    num += 1
print(num-1)