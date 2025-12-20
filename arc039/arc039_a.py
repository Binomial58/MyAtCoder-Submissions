a, b = map(str, input().split())
A = [int(a[i]) for i in range(3)]
B = [int(b[i]) for i in range(3)]
M = int(a) - int(b)
for i in range(3):
    # Aを大きくする
    C = [A[i] for i in range(3)]
    C[i] = 9
    a = 100 * C[0] + 10 * C[1] + C[2]
    b = 100 * B[0] + 10 * B[1] + B[2]
    M = max(M, a - b)
    # Bを小さくする
    C = [B[i] for i in range(3)]
    if i == 0:
        C[i] = 1
    else:
        C[i] = 0
    a = 100 * A[0] + 10 * A[1] + A[2]
    b = 100 * C[0] + 10 * C[1] + C[2]
    M = max(M, a - b)
print(M)