n = int(input())
s = input()
E = [0]
W = [0]
for i in range(n):
    if s[i] == "E":
        E.append(1)
        W.append(0)
    else:
        E.append(0)
        W.append(1)
for i in range(1, n + 1):
    E[i] += E[i - 1]
    W[i] += W[i - 1]
# print(E)
# print(W)
minp = 10**10
for i in range(1, n + 1):
    minp = min(minp, W[i - 1] + E[-1] - E[i])
    # print(minp)
print(minp)
