n = int(input())
A = list(map(int, input().split()))
ans = 10**10
D = dict()
for i in range(n):
    if A[i] in D:
        ans = min(ans, i - D[A[i]] + 1)
    D[A[i]] = i
if ans == 10**10:
    print(-1)
else:
    print(ans)
