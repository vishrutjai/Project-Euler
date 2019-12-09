#a, b, c = 0, 0, 0
flag = 0
for x in range(1,1001):
    for y in range(1,1001):
        z = 1000 - x - y
        l = [x, y, z]
        l.sort()
        if l[-1]**2 == (l[0]**2) + (l[1]**2):
            print(l[0] * l[1] * l[2])
            flag = 1
            break
    if flag == 1:
        break

        
        