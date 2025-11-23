n, a, b, c, d = map(int, input().split())
sx = a + b
sy = c + d
ex = a + c
ey = b + d
if abs(sx - ex) <= 1 and abs(sy - ey) <= 1:
    if a != 0 and d != 0:
        if b != 0 or c != 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
else:
    print("No")
