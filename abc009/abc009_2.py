n = int(input())
A = []
for i in range(n):
    A.append(int(input()))
A = list(set(A))
A.sort(reverse=True)
print(A[1])
