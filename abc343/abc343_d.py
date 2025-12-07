n, t = map(int, input().split())
R = []
# それぞれの点数を管理する配列
B = [0 for i in range(n)]
# 点数の個数を管理する辞書
C = {0: n}
for i in range(t):
    a, b = map(int, input().split())
    C[B[a - 1]] -= 1
    if C[B[a - 1]] == 0:
        del C[B[a - 1]]
    B[a - 1] += b
    if B[a - 1] not in C:
        C[B[a - 1]] = 1
    else:
        C[B[a - 1]] += 1
    R.append(len(C))
for r in R:
    print(r)
