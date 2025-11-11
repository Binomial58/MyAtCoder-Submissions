I = list(map(int, input().split()))
count = 0
while I.count(I[0]) != 3:
    I.sort()
    if I[2] - I[0] >= 2:
        I[0] += 2
    else:
        I[0] += 1
        I[1] += 1
    count += 1
print(count)
