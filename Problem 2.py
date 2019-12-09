a = -1
b = 1
count = 0
while a+b <= 4000001:
    print(a+b)
    if (a+b) % 2 == 0:
        count += a+b
    a, b = b, a + b
print(count)

