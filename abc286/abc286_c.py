n, a, b = map(int, input().split())
s = input()
s = s + s
# print(s)
left = 0
right = n
now = 10**20
for i in range(n):
    t = s[left:right]
    u = t[::-1]
    # print(t, u)
    # print(t, u)
    count = 0
    for j in range(n):
        # print(j)
        if t[j] != u[j]:
            count += b
    count //= 2
    count += i * a
    # print(t)
    left += 1
    right += 1
    # print(count)
    now = min(now, count)
print(now)
