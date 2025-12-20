n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
R = [[], []]
now = 0
for i in range(n):
    if A[i] == B[now]:
        R[0].append(i)
        now += 1
    if now == m:
        break
now = m - 1
for i in range(n - 1, -1, -1):
    if A[i] == B[now]:
        R[1].append(i)
        now -= 1
    if now == -1:
        break
R[1] = R[1][::-1]
if len(R[0]) != m:
    print("No")
else:
    if R[0] == R[1]:
        print("No")
    else:
        print("Yes")
# print(R[0])
# print(R[1])
