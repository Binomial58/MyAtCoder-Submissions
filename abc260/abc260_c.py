n, x, y = map(int, input().split())
R = [0 for i in range(n)]
B = [0 for i in range(n)]
R[n - 1] = 1
for i in range(n):
    for j in range(n - 1, 0, -1):
        R[j - 1] += R[j]
        B[j] += R[j] * x
        R[j] = 0
    # print(R)
    # print(B)
    for j in range(n - 1, 0, -1):
        R[j - 1] += B[j]
        B[j - 1] += B[j] * y
        B[j] = 0
    # print(R)
    # print(B)
# print(R)
# print(R)
# print(B)
print(B[0])
