n, q = map(int, input().split())
Xnow = [i for i in range(1, n + 1)]
X = [int(input()) for i in range(q)]
Xi = dict()
for i in range(n):
    Xi[i + 1] = i
for x in X:
    # d,e：スワップするもの
    d = Xi[x]
    if d == n - 1:
        e = d - 1
    else:
        e = d + 1
    dn = Xnow[d]
    en = Xnow[e]
    Xnow[d] = en
    Xnow[e] = dn
    Xi[en] = d
    Xi[dn] = e
    # print(dn, en)
    # print(Xnow)
    # print(Xi)
# print(Xi)
print(*Xnow)