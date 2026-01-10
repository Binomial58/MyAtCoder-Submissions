n, w = map(int, input().split())
Q = []
mt = 0
for i in range(n):
    Q.append(list(map(int, input().split())))
    mt = max(mt, Q[-1][1])
W = [0 for i in range(mt + 1)]
for i in range(n):
    s, t, p = Q[i]
    W[s] += p
    W[t] -= p
for i in range(1, mt + 1):
    W[i] += W[i - 1]
if max(W) > w:
    print("No")
else:
    print("Yes")
# print(W)
