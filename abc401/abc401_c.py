n, k = map(int, input().split())
F = [1] * k
if n < k:
    print(1)
    exit()
F.append(k)
s = k
for i in range(n - k):
    s = s + F[-1] - F[i]
    s %= 10**9
    F.append(s)
print(F[-1])
