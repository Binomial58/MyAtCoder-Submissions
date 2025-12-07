n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
if A[0] == 1 or A[-1] == n:
    print(-1)
    exit()
else:
    A = set(A)
    B = []
    for i in range(1, n + 1):
        if i not in A:
            B.append(i)
    B = set(B)
    i = 1
    C = []
    # A,Bで連続している数
    a = 0
    b = 0
    while i != n + 1:
        if i in A:
            if b != 0:
                b = 0
                # BからAに切り替わった直後は数を保留する．
                c = i
            else:
                b = 0
                C.append(i)
            a += 1
        else:
            C.append(i)
            if a != 0:
                a = 0
                C.append(c)
            b += 1
        i += 1
print(*C)
