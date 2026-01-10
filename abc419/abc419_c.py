n = int(input())
G = [[], []]
for i in range(n):
    r, c = map(int, input().split())
    G[0].append(r)
    G[1].append(c)
g = max(max(G[0]) - min(G[0]), max(G[1]) - min(G[1]))
if g % 2 == 0:
    print(g // 2)
else:
    print(g // 2 + 1)
