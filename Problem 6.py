sum = 0
sumofsquares = 0
a = 1
while a != 101:
    sum += a
    sumofsquares += (a**2)
    a += 1

sum = sum ** 2
print(sum - sumofsquares)