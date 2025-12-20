from collections import Counter

n = int(input())
A = list(map(int, input().split()))
B = Counter(A)
count = 1
for i in range(n):
    if i != n - 1 and A[i] != A[i + 1]:
        count += n - i - B[A[i]]
    B[A[i]] -= 1
print(count)
