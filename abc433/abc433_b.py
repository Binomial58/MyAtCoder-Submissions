n = int(input())
A = list(map(int, input().split()))
A = [-1] + A
for i in range(1, n + 1):
    m = -1
    for j in range(i):
        if A[j] > A[i]:
            m = j
    print(m)
