n, k = map(int, input().split())
P = list(map(int, input().split()))
# Pの期待値を格納する配列
Pe = []
for p in P:
    Pe.append(((1 + p) / 2))
# Peの累積和を格納する配列
Psum = [0] + [Pe[i] for i in range(n)]
for i in range(1, n + 1):
    Psum[i] += Psum[i - 1]
# print(Psum)
m = 0
for i in range(n - k + 1):
    m = max(m, Psum[i + k] - Psum[i])
print(m)