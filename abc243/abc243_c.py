n = int(input())
G = []
for i in range(n):
    Z = list(map(int, input().split()))
    G.append(Z)
s = input()
# 右を向いている方
R = dict()
Rs = set()
# 左を向いている方
L = dict()
Ls = set()
for i in range(n):
    x = G[i][0]
    y = G[i][1]
    if s[i] == "R":
        if y in Rs:
            R[y] = min(R[y], x)
        else:
            R[y] = x
            Rs.add(y)
    if s[i] == "L":
        if y in Ls:
            L[y] = max(L[y], x)
        else:
            L[y] = x
            Ls.add(y)
S = Rs & Ls
for t in S:
    r = R[t]
    l = L[t]
    if r < l:
        print("Yes")
        exit()
# print(R)
# print(L)
# print(S)
print("No")
