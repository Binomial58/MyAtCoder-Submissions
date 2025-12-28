n, k, s = map(int, input().split())
A = [s] * k
# print(A)
for i in range(n - k):
    if s == 10**9:
        A.append(10**9 - 1)
    else:
        A.append(10**9)
print(*A)
