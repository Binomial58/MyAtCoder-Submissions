n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
now = -1
j = 0
for i in range(n):
    if j != n - 1 and A[i] <= B[j]:
        j += 1
    else:
        if now != -1:
            print(-1)
            exit()
        else:
            now = A[i]
print(now)
