a, b, c = map(int, input().split())
a %= 10
b %= 4
# b^c mod 4 を計算したい
T = [[i] for i in range(10)]
for i in range(10):
    for j in range(10):
        if (T[i][-1] * i) % 10 not in T[i]:
            T[i].append((T[i][-1] * i) % 10)
        else:
            break
S = [[i] for i in range(4)]
for i in range(4):
    for j in range(4):
        if (S[i][-1] * i) % 4 not in S[i]:
            S[i].append((S[i][-1] * i) % 4)
        else:
            break
# mを計算する
if len(S[b]) == 1:
    m = S[b][0]
else:
    if b == 2:
        if c == 1:
            m = 2
        else:
            m = 0
    else:
        m = S[b][(c - 1) % 2]
# print(m)
# modを計算する
if len(T[a]) == 1:
    print(T[a][0])
elif len(T[a]) == 2:
    print((T[a][(m - 1) % 2]))
else:
    print((T[a][(m - 1) % 4]))
# print(T)
# print(S)
