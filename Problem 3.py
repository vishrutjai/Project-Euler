def prime(n):
    flag = 0
    for x in range(2, int(n**(1/2))+1):
        if n % x == 0:
            flag = 1
            return False
    if flag == 0:
        return True

count = 0
n = 0
for x in range(1, 600851475143+1):
    if 600851475143 % x == 0:
        if prime(x) == True:
            #print(x)
            n = x
            #count += x
print(n)