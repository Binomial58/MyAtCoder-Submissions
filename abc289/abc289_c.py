n, m = map(int, input().split())
A = []
for i in range(m):
    c = int(input())
    A.append(set(list(map(int, input().split()))))
ans = set(i + 1 for i in range(n))
count = 0
for i in range(1 << m):
    s = set()
    for j in range(m):
        if (i >> j) & 1:
            s |= A[j]
    if ans == s:
        count += 1
print(count)
