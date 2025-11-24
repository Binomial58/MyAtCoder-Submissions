n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
Buy = []
i = 0
for b in B:
    while i != n and b > A[i]:
        i += 1
    if i == n:
        print(-1)
        exit()
    Buy.append(A[i])
    i += 1
    # print(Buy)
if len(Buy) != m:
    print(-1)
else:
    # print(Buy)
    print(sum(Buy))
