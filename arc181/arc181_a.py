t = int(input())
R = []
for i in range(t):
    n = int(input())
    P = list(map(int, input().split()))
    # 0回の操作でできるかの確認
    if P == [i + 1 for i in range(n)]:
        R.append(0)
    else:
        # 1回の操作でできるかの確認
        mP = [P[i] for i in range(n)]
        MP = [P[i] for i in range(n)]
        for i in range(1, n):
            mP[i] = min(mP[i], mP[i - 1])
            MP[i] = max(MP[i], MP[i - 1])
        for k in range(n):
            if mP[k] == 1 and MP[k] == k + 1 and P[k] == k + 1:
                R.append(1)
                break
        else:
            if P[0] == n and P[-1] == 1:
                R.append(3)
            else:
                R.append(2)
for r in R:
    print(r)
