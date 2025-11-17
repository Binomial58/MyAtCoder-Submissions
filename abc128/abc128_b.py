n = int(input())
S = []
P = []
N = [i + 1 for i in range(n)]
for i in range(n):
    s, p = map(str, input().split())
    S.append(s)
    P.append(int(p))
name = list(set(S))
name.sort()
city = {}
for na in name:
    city[na] = []
for i in range(n):
    city[S[i]].append([P[i], i + 1])
for c in name:
    T = city[c]
    T.sort(reverse=True)
    for t in T:
        print(t[1])
