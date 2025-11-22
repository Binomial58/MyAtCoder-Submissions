import itertools

n, k = map(int, input().split())
T = [list(map(int, input().split())) for i in range(n)]
count = 0
Path = [i for i in range(1, n)]
for p in itertools.permutations(Path):
    now = T[0][p[0]] + T[0][p[-1]]
    for i in range(n - 2):
        now += T[p[i]][p[i + 1]]
    if now == k:
        count += 1
print(count)
