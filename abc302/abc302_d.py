import bisect

n, m, d = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
# print(A)
# print(B)
ans = -1
for a in A:
    i = bisect.bisect(B, a - d)
    j = bisect.bisect(B, a + d)
    if i != j:
        ans = max(ans, B[j - 1] + a)
    else:
        if i != 0:
            if abs(a - B[i - 1]) <= d:
                ans = max(ans, a + B[i - 1])
    # print(i, j)
print(ans)
