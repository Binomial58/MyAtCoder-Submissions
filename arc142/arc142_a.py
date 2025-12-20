n, k = map(int, input().split())
count = 0
a = str(k)
b = a[::-1]
a = int(a)
b = int(b)
if str(k)[-1] == "0" or a > b:
    print(0)
else:
    while n >= a:
        count += 1
        a *= 10
    while n >= b:
        # if b >= k:
        count += 1
        # print(b)
        b *= 10
    if a == b:
        print(count // 2)
    else:
        print(count)
