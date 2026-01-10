n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
if m > n:
    print("NO")
else:
    i = 0
    j = 0
    while i != n and j != m:
        if B[j] <= A[i]:
            i += 1
            j += 1
        else:
            i += 1
    if j == m:
        print("YES")
    else:
        print("NO")
