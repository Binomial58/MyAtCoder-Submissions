n = int(input())
S = []
for i in range(n):
    S.append(input())
m = int(input())
T = []
for i in range(m):
    T.append(input())
now = 0
item = set(S)
for s in item:
    count = S.count(s) - T.count(s)
    now = max(now, count)
print(now)
