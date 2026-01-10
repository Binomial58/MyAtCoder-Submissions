n, m = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
D = []
for i in range(m - 1):
    D.append(X[i + 1] - X[i])
D.sort(reverse=True)
# print(D)
print(sum(D) - sum(D[: n - 1]))
