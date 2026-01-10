n = int(input())
A = list(map(int, input().split()))
for i in range(n - 1):
    if A[i] >= A[i + 1]:
        print("No")
        exit()
print("Yes")
