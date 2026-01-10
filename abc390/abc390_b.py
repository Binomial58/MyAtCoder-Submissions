n = int(input())
A = list(map(int, input().split()))
if n == 2:
    print("Yes")
    exit()
for i in range(len(A) - 2):
    if A[i] * A[i + 2] != A[i + 1] ** 2:
        print("No")
        exit()
print("Yes")
