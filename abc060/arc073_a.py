n, t = map(int, input().split())
T = list(map(int, input().split()))
count = 0
now = 0
for i in T:
    if now <= i:
        count += t
    else:
        count -= now - i
        count += t
    now = i + t
print(count)
