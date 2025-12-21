l, r = map(int, input().split())
m = 10**10
for i in range(l, min(r + 1, l + 2020)):
    for j in range(l, min(r + 1, l + 2020)):
        if i != j:
            m = min(m, (i * j) % 2019)
    # print(i)
print(m)
