n = int(input())
A = list(map(int, input().split()))
An = dict()
As = set()
for a in A:
    for j in range(-1, 2):
        As.add(a + j)
        if a + j not in An:
            An[a + j] = 1
        else:
            An[a + j] += 1
m = 0
for s in As:
    m = max(m, An[s])
print(m)
