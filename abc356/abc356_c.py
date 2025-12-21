n, m, k = map(int, input().split())
A = []
R = []
for i in range(m):
    A.append([])
    C = list(map(str, input().split()))
    for i in range(int(C[0])):
        A[-1].append(int(C[1 + i]) - 1)
    if C[-1] == "o":
        R.append(1)
    else:
        R.append(0)
count = 0
for i in range(1 << n):
    K = [0 for i in range(n)]
    for j in range(n):
        if (i >> j) & 1:
            K[j] = 1
    flag = True
    for j in range(m):
        c = 0
        for a in A[j]:
            c += K[a]
        if R[j] == 1 and c < k:
            flag = False
        elif R[j] == 0 and c >= k:
            flag = False
    if flag:
        count += 1
        # print(K)
# print(A)
# print(R)
print(count)
