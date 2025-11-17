n, t = map(int, input().split())
A = list(map(int, input().split()))
now = [0 for i in range(2 * n + 2)]
count = 0
for a in A:
    count += 1
    h = (a - 1) // n
    w = (a - 1) % n
    now[w] += 1
    now[n + h] += 1
    if h == w:
        now[2 * n] += 1
    if h + w == n - 1:
        now[-1] += 1
    if now[w] == n or now[n + h] == n or now[2 * n] == n or now[-1] == n:
        print(count)
        exit()
print(-1)
