n = int(input())
A = list(map(int, input().split()))
if n == 1:
    print(1)
    exit()
D = []
for i in range(n - 1):
    D.append(A[i + 1] - A[i])
now = D[0]
count = 1
E = []
for i in range(1, n - 1):
    if D[i] == now:
        count += 1
    else:
        E.append(count)
        now = D[i]
        count = 1
E.append(count)
r = 0
for e in E:
    r += (e + 1) * (e + 2) // 2
r -= len(E) - 1
print(r)
