X = list(map(int, input().split()))
Y = list(map(int, input().split()))
count = 0
V = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
for v in V:
    m = 1
    for i in range(3):
        m *= X[i] // Y[v[i]]
    count = max(count, m)
print(count)
