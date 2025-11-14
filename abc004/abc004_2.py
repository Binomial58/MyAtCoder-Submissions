C = [(input()) for _ in range(4)]
D = [[] for i in range(4)]
for i in range(3, -1, -1):
    for j in range(3, -1, -1):
        D[3 - i].append(C[i][j * 2])
for d in D:
    print(*d)
