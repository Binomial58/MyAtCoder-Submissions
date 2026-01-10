n = int(input())
A = list(map(int, input().split()))
R = [0] * n
for i in range(n - 1):
    if A[i] > A[i + 1]:
        R[i] ^= 1
        R[i + 1] ^= 1
print(*R)
