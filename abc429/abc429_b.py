n, m = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)
for i in range(n):
    if s - A[i] == m:
        print("Yes")
        exit()
print("No")
