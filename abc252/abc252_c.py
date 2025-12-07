n = int(input())
S = [input() for i in range(n)]
# 各数字がどの位置にどのくらい出てくるのか
D = [[0 for i in range(10)] for i in range(10)]
for i in range(n):
    for j in range(10):
        D[int(S[i][j])][j] += 1
m = 10**10
for i in range(10):
    c = 0
    E = D[i]
    j = max(E)
    c += 10 * (j - 1)
    k = E[::-1].index(j)
    c += 9 - k
    m = min(c, m)
print(m)
