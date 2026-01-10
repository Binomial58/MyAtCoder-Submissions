n, m = map(int, input().split())
A = list(map(int, input().split()))
S = set(i + 1 for i in range(m))
for i in range(n):
    if set(A) != S:
        print(i)
        exit()
    A.pop()
print(n)
