n, a, b = map(int, input().split())
now = 0
for i in range(n):
    s, d = map(str, input().split())
    d = int(d)
    if s == "East":
        if d < a:
            now += a
        elif d > b:
            now += b
        else:
            now += d
    else:
        if d < a:
            now -= a
        elif d > b:
            now -= b
        else:
            now -= d
if now > 0:
    print("East", now)
elif now < 0:
    print("West", -now)
else:
    print(0)
