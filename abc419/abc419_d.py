n, m = map(int, input().split())
s = input()
t = input()
S = [0 for i in range(n + 1)]
for i in range(m):
    l, r = map(int, input().split())
    S[l - 1] += 1
    S[r] -= 1
sumS = [0 for i in range(n + 1)]
sumS[0] = S[0]
for i in range(n):
    sumS[i + 1] = sumS[i] + S[i + 1]
C = []
for i in range(n):
    if sumS[i] % 2 == 0:
        C.append(s[i])
    else:
        C.append(t[i])
print("".join(C))
