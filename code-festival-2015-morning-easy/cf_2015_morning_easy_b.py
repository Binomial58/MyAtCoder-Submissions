n = int(input())
s = input()
if n % 2 == 1:
    print(-1)
else:
    t = s[: n // 2]
    u = s[n // 2 :]
    count = 0
    for i in range(n // 2):
        if t[i] != u[i]:
            count += 1
    print(count)
