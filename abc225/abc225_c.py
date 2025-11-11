n, m = map(int, input().split())
B = []
for i in range(n):
    B.append(list(map(int, input().split())))
p = B[0][0] // 7
r = B[0][0] % 7
C = []
for b in B[0]:
    C.append((b - 1) % 7)
for i in range(m - 1):
    if C[i] > C[i + 1] or B[0][i + 1] - B[0][i] != 1:
        print("No")
        exit()
for j in range(n - 1):
    for i in range(m):
        if B[j + 1][i] != B[j][i] + 7:
            print("No")
            exit()
print("Yes")
