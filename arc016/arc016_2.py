def rle(S):
    N = len(S)
    i = 0
    while i < N:
        j = i
        while j < N and S[i] == S[j]:
            j += 1
        yield S[i], j - i
        i = j


# list(rle(s))のようにリストで受け取る


n = int(input())
X = [list(input()) for _ in range(n)]
Xt = [[] for i in range(9)]
for i in range(9):
    for j in range(n):
        Xt[i].append(X[j][i])
# for x in Xt:
#     print(x)
count = 0
for i in range(9):
    T = list(rle(Xt[i]))
    for t in T:
        if t[0] == "o":
            count += 1
        elif t[0] == "x":
            count += t[1]
print(count)
# print(T)
