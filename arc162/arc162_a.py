t = int(input())
R = []
for i in range(t):
    n = int(input())
    C = [i for i in range(1, n + 1)]
    P = list(map(int, input().split()))
    count = 0
    for i in range(n):
        flag = True
        for j in range(n):
            if i < j:
                if P[i] > P[j]:
                    flag = False
        if flag:
            count += 1
    R.append(count)
    # print(D)
for r in R:
    print(r)