t = int(input())
R = []
for i in range(t):
    A = list(map(int, input().split()))
    C = [0, 0, 0, 0, 0]
    for i in range(4):
        C[i] = min(A[i], A[8 - i])
    C[4] = A[4] // 2
    if C.count(0) == 5:
        R.append(0)
    else:
        if C[4] == max(C):
            c = A[4]
            R.append(max(0, 2 * c - sum(A) - 1))
        else:
            if A.count(0) == 7:
                R.append(1)
            else:
                R.append(0)
        # print(C)
for r in R:
    print(r)
