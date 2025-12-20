s = input()
k = int(input())
count = 0
if len(s) == 1:
    print(k // 2)
elif len(s) == 2:
    if s[0] == s[1]:
        print(k)
    else:
        print(0)
else:
    W = []
    l = 1
    a = s[0]
    for i in range(1, len(s)):
        if s[i] == a:
            l += 1
        else:
            W.append([a, l])
            a = s[i]
            l = 1
    W.append([a, l])
    # print(W)
    if s[0] == s[-1]:
        if len(W) != 1:
            count += (W[0][1] + W[-1][1]) // 2
            for i in range(1, len(W) - 1):
                count += W[i][1] // 2
            count *= k - 1
            for i in range(len(W)):
                count += W[i][1] // 2
        else:
            if len(s) % 2 == 0:
                count += len(s) // 2 * k
            else:
                count += (len(s) // 2 + 1) * (k // 2)
                count += (len(s) // 2) * (k - k // 2)
    else:
        for i in range(len(W)):
            count += W[i][1] // 2
        count *= k
    print(count)
