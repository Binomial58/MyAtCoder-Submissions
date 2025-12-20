n = int(input())
L, R = [], []
for i in range(n):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
if sum(L) <= 0 <= sum(R):
    print("Yes")
    Re = []
    s = -sum(L)
    for i in range(n):
        if R[i] - L[i] <= s:
            Re.append(R[i])
            s -= R[i] - L[i]
        elif s != 0:
            Re.append(L[i] + s)
            s = 0
        else:
            Re.append(L[i])
    print(*Re)
else:
    print("No")
