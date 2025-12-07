n, m, h, k = map(int, input().split())
s = input()
I = set()
for i in range(m):
    G = list(map(int, input().split()))
    I.add((G[0], G[1]))
x = 0
y = 0
vec = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
for i in range(n):
    v = vec[s[i]]
    x += v[0]
    y += v[1]
    h -= 1
    if h < 0:
        print("No")
        exit()
    if h < k and (x, y) in I:
        h = k
        I.remove((x, y))
print("Yes")
