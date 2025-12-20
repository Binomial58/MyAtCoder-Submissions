n, k = map(int, input().split())
A = list(map(int, input().split()))
V = [[] for i in range(k)]
for i in range(n):
    V[i % k].append(A[i])
for i in range(k):
    V[i].sort()
M = []
count = 0
for i in range(n):
    M.append(V[i % k][count])
    if i % k == k - 1:
        count += 1
A.sort()
if A == M:
    print("Yes")
else:
    print("No")
