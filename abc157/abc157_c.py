n, m = map(int, input().split())
A = [0 for i in range(n)]
if n != 1:
    A[0] = 1
B = [True for i in range(n)]
flag = True
for i in range(m):
    s, c = map(int, input().split())
    if B[s - 1] or A[s - 1] == c:
        A[s - 1] = c
        B[s - 1] = not B[s - 1]
    else:
        flag = not flag
for i in range(n):
    A[i] = str(A[i])
if flag:
    if n != 1 and A[0] == "0":
        print(-1)
    else:
        print(int("".join(A)))
else:
    print(-1)
