n, l = map(int, input().split())
S = [input() for i in range(n)]
S.sort()
t = ""
for s in S:
    t += s
print(t)
