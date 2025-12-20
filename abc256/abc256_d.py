import bisect

n = int(input())
L, R = [], []
for i in range(n):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
L, R = zip(*sorted(zip(L, R)))
L = list(L)
R = list(R)
for i in range(1, n):
    R[i] = max(R[i], R[i - 1])
# print(L)
# print(R)
# 答えを格納する配列
Bob = [[-1, -1]]
i = 0
j = 0
if n == 1:
    print(l, r)
else:
    while i != n - 1:
        i = j
        a = L[i]
        if Bob[-1] == [-1, -1]:
            Bob[-1][0] = a
        b = R[i]
        j = bisect.bisect(L, b) - 1
        # print(i, j)
        if i == j:
            Bob[-1][1] = b
            if i != n - 1:
                Bob.append([-1, -1])
                j += 1
    for b in Bob:
        print(*b)
