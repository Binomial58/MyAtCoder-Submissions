n = int(input())
H = list(map(int, input().split()))
count = 0
t = 0
for i in range(n):
    if t == 1:
        if H[i] == 1:
            H[i] -= 1
            t = 2
            count += 1
        else:
            H[i] = max(0, H[i] - 4)
            t = 0
            count += 2
    elif t == 2:
        H[i] = max(0, H[i] - 3)
        t = 0
        count += 1
    if H[i] // 5 != 0:
        t = 0
    count += H[i] // 5 * 3
    H[i] %= 5
    while H[i] != 0:
        if t != 2:
            H[i] -= 1
            t += 1
        else:
            H[i] = max(0, H[i] - 3)
            t = 0
        count += 1
    # print(H[i], count)
    # print(t)
# print(H)
print(count)
