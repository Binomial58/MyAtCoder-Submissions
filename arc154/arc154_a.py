n = int(input())
a = input()
b = input()
A = [a[i] for i in range(n)]
B = [b[i] for i in range(n)]
T = [[] for i in range(n // 10 + 1)]
a = 0
b = 0
for i in range(n):
    a *= 10
    b *= 10
    if int(A[i]) >= int(B[i]):
        A[i], B[i] = B[i], A[i]
    a += int(A[i])
    b += int(B[i])
    a %= 998244353
    b %= 998244353
print(a * b % 998244353)
