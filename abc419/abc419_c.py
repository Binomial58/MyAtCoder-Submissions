def Chebyshev(x1, y1, x2, y2):
    return max(abs(x1 - x2), abs(y1 - y2))


n = int(input())
R = []
C = []
for i in range(n):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)
d = max(max(R) - min(R), max(C) - min(C))
if d % 2 == 0:
    print(d // 2)
else:
    print(d // 2 + 1)
