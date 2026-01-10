n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for b in B:
    if b in A:
        id = A.index(b)
        A = A[:id] + A[id + 1 :]
print(*A)
