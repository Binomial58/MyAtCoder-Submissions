t = int(input())
R = []
for i in range(t):
    n = int(input())
    d = n
    A = []
    while d >= 2:
        A.append(d % 2)
        d //= 2
    A.append(d)
    A = A[::-1]
    # print(A)
    c = A.count(1)
    if c == 3:
        now = n
        R.append(n)
    elif c > 3:
        # 1を削除する回数
        m = c - 3
        j = len(A) - 1
        while m != 0:
            if A[j] == 1:
                A[j] = 0
                m -= 1
            j -= 1
        now = 0
        for j in range(len(A)):
            now += A[j] * 2 ** (len(A) - j - 1)
        R.append(now)
    else:
        # 1を追加する回数
        m = 3 - c
        if len(A) <= 3:
            # print(len(A), n)
            now = -1
            R.append(-1)
        else:
            if c == 1:
                A[0] = 0
                for j in range(1, 4):
                    A[j] = 1
            else:
                count = 0
                for j in range(len(A)):
                    if A[j] == 1:
                        count += 1
                    if count == 2:
                        id = j
                        break
                if id == len(A) - 1 or id == len(A) - 2:
                    A[id] = 0
                    A[0] = 0
                    for j in range(1, 4):
                        A[j] = 1
                else:
                    # print(id)
                    A[id] = 0
                    A[id + 1] = 1
                    A[id + 2] = 1
            now = 0
            for j in range(len(A)):
                now += A[j] * 2 ** (len(A) - j - 1)
            R.append(now)
    # print(now)
    # print(A)
for r in R:
    print(r)
