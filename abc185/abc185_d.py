import math

n, m = map(int, input().split())
A = list(map(int, input().split()))
A = [0] + A + [n + 1]
A.sort()
G = []
for i in range(len(A) - 1):
    if A[i + 1] - A[i] != 1:
        G.append(A[i + 1] - A[i] - 1)
if G != []:
    k = min(G)
else:
    print(0)
    exit()
count = 0
for g in G:
    count += math.ceil(g / k)
print(count)
# print(G)
# print(A)
