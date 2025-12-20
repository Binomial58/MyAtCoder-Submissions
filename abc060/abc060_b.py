a, b, c = map(int, input().split())
now = a % b
M = [now]
while True:
    now += a
    now %= b
    # print(M)
    if now == c:
        print("YES")
        exit()
    else:
        if now in M:
            print("NO")
            exit()
        else:
            M.append(now)
