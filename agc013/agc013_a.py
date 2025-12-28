n = int(input())
A = list(map(int, input().split()))
count = 0
now = A[0]
c = 0
d = 0
for i in range(n):
    if c == 0:
        c += 1
        d = 0
        count += 1
    elif c == 1 or d == 0:
        if A[i] - now > 0:
            d = 1
        elif A[i] - now < 0:
            d = -1
        c += 1
    else:
        if (A[i] - now) * d < 0:
            c = 1
            d = 0
            count += 1
        else:
            c += 1
    now = A[i]
    # print(d, c, A[i] - now)
print(count)
