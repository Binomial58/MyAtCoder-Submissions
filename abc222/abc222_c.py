n, m = map(int, input().split())
A = []
R = [[i, 0] for i in range(1, 2 * n + 1)]
Rank = [R[i][0] - 1 for i in range(2 * n)]
for i in range(2 * n):
    A.append(input())
for i in range(m):
    for j in range(n):
        a = R[2 * j][0] - 1
        b = R[2 * j + 1][0] - 1
        ai = Rank.index(a)
        bi = Rank.index(b)
        # print(a + 1, b + 1)
        # print(A[a][i], A[b][i])
        if A[a][i] == "G":
            if A[b][i] == "C":
                R[ai][1] += 1
            elif A[b][i] == "P":
                R[bi][1] += 1
        elif A[a][i] == "C":
            if A[b][i] == "P":
                R[ai][1] += 1
            elif A[b][i] == "G":
                R[bi][1] += 1
        else:
            if A[b][i] == "G":
                R[ai][1] += 1
            elif A[b][i] == "C":
                R[bi][1] += 1
    R.sort(key=lambda x: (-x[1], x[0]))
    # print(R)
    Rank = [R[i][0] - 1 for i in range(2 * n)]
for r in R:
    print(r[0])
