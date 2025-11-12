n, m = map(int, input().split())
A = []
B = []
for i in range(n):
    A.append(input())
for i in range(m):
    B.append(input())
for i in range(n - m + 1):
    for j in range(n - m + 1):
        flag = m**2
        for a in range(m):
            for b in range(m):
                if B[b][a] == A[b + i][a + j]:
                    flag -= 1
        if flag == 0:
            print("Yes")
            exit()
print("No")
