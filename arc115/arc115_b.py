n = int(input())
C = []
mid = 10**10
for i in range(n):
    t = list(map(int, input().split()))
    if min(t) < mid:
        mid = min(mid, min(t))
        id = i
    C.append(t)
D = [C[0][i + 1] - C[0][i] for i in range(n - 1)]
E = [C[i + 1][0] - C[i][0] for i in range(n - 1)]
# print(D)
# print(E)
for i in range(1, n):
    for j in range(1, n):
        if C[i][j] - C[i][j - 1] != D[j - 1] or C[j][i] - C[j - 1][i] != E[j - 1]:
            print("No")
            exit()
A = [C[id][i] - mid for i in range(n)]
B = []
for i in range(n):
    B.append(C[i][0] - A[0])
print("Yes")
print(*B)
print(*A)
