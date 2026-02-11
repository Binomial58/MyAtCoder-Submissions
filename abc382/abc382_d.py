def dfs(D):
    if len(D) == n:
        Ans.append([])
        for j in range(n):
            Ans[-1].append(D[j])
    else:
        for i in range(10):
            if D[-1] + 10 + i <= A[len(D)]:
                D.append(D[-1] + 10 + i)
                dfs(D)
                D.pop()


n, m = map(int, input().split())
Ans = []
# 各桁で許される最大の数
A = [m - 10 * (n - 1) + 10 * i for i in range(n)]
# print(A)
for j in range(1, A[0] + 1):
    dfs([j])
# print(Ans)
print(len(Ans))
for ans in Ans:
    print(*ans)
