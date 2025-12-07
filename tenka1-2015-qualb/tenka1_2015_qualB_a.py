A = [0 for i in range(20)]
A[0] = 100
A[1] = 100
A[2] = 200
for i in range(3, 20):
    A[i] = A[i - 1] + A[i - 2] + A[i - 3]
print(A[-1])
