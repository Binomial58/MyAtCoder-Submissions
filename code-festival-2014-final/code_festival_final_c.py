a = int(input())
k = 10
while True:
    f = 0
    t = str(k)
    for i in range(len(t)):
        f += k ** (len(t) - i - 1) * int(t[i])
    if f == a:
        print(k)
        exit()
    if f > a:
        print(-1)
        exit()
    k += 1
