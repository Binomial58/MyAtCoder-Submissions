import bisect

n, q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
Rs = [0 for i in range(n)]
Rs[0] = R[0]
for i in range(1, n):
    Rs[i] = Rs[i - 1] + R[i]
# print(Rs)
Ans = []

for _ in range(q):
    x = int(input())
    id = bisect.bisect(Rs, x)
    Ans.append(min(id, x))
for a in Ans:
    print(a)
