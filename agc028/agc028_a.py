import math

n, m = map(int, input().split())
s = input()
t = input()
l = math.lcm(n, m)
if s[0] != t[0]:
    print(-1)
else:
    flag = True
    if m > n:
        m, n = n, m
        s, t = t, s
    T = math.lcm(l // n, l // m)
    # print(T)
    for i in range(l // T):
        # print(s[(l // m) * i], t[(l // n) * i])
        if s[(l // m) * i] != t[(l // n) * i]:
            flag = False
            break
    if flag:
        print(l)
    else:
        if math.gcd(n, m) == 1:
            print(n * m)
        else:
            print(-1)
