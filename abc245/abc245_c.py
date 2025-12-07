n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = A[0]
b = B[0]
for i in range(1, n):
    c = a
    d = b
    if c - k <= A[i] <= c + k or d - k <= A[i] <= d + k:
        a = A[i]
    else:
        a = -(10**10)
    if c - k <= B[i] <= c + k or d - k <= B[i] <= d + k:
        b = B[i]
    else:
        b = -(10**10)
    # print(a, b)
    if a == -(10**10) and b == -(10**10):
        print("No")
        exit()
print("Yes")
