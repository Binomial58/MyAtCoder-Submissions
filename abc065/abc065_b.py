n = int(input())
A = []
for i in range(n):
    A.append(int(input()) - 1)
B = [True for i in range(n)]
now = 0
count = 0
while B[now] and now != 1:
    count += 1
    B[now] = not B[now]
    now = A[now]
if now == 1:
    print(count)
else:
    print(-1)
