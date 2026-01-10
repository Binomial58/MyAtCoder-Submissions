n, m = map(int, input().split())
s = input()
t = input()
mi = 10**10
for i in range(n - m + 1):
    a = s[i : i + m]
    now = 0
    # print(a)
    for j in range(m):
        # print(a[j], t[j])
        if int(a[j]) - int(t[j]) < 0:
            now += int(a[j]) - int(t[j]) + 10
        else:
            now += int(a[j]) - int(t[j])
        # print(now)
    # print(a)
    # print(t)
    mi = min(now, mi)
print(mi)
