x, y = map(int, input().split())
d = (x + y) % 12
if d == 0:
    print(12)
else:
    print(d)
