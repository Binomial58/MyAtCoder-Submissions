n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
i = 0
count = 0
now = k
while now != 0:
    now = min(A.count(i), now)
    i += 1
    count += now
print(count)
