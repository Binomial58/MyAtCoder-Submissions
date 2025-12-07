import math

r, x, y = map(int, input().split())
e = math.sqrt(x**2 + y**2)
if x**2 + y**2 == r**2:
    print(1)
elif x**2 + y**2 <= r**2:
    print(2)
else:
    print(math.ceil(e / r))
