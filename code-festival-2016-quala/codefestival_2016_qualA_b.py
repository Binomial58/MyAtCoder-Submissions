n = int(input())
A = list(map(int, input().split()))
for i in range(n):
    A[i] -= 1
count = 0
for i in range(n):
    if i > A[i] and A[A[i]] == i:
        count += 1
print(count)
