n = int(input())
P = list(map(int, input().split()))
for i in range(n - 1, -1, -1):
    if P[i - 1] > P[i]:
        k = i - 1
        break
R = P[:k]
T = P[k:]
T.sort()
u = T.index(P[k])
R.append(T[T.index(P[k]) - 1])
T.pop(T.index(P[k]) - 1)
T.sort(reverse=True)
for t in T:
    R.append(t)
print(*R)
