n = int(input())
A = list(map(int, input().split()))
for i in range(n):
    A[i] -= 1
isDone = [False for i in range(n)]
i = 0
B = []
while True:
    if not isDone[i]:
        isDone[i] = True
        B.append(i + 1)
        i = A[i]
    if isDone[i]:
        B.append(i + 1)
        break
e = B[-1]
ei = B.index(e)
print(len(B[ei + 1 :]))
print(*B[ei + 1 :])
