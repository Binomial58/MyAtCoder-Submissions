n = int(input())
n %= 30
A = [1, 2, 3, 4, 5, 6]
for i in range(n):
    a = i % 5
    b = i % 5 + 1
    A[a], A[b] = A[b], A[a]
    # if A == [1, 2, 3, 4, 5, 6]:
    #     print(i + 1)
    # print(i + 1, A)
for i in range(6):
    A[i] = str(A[i])
print("".join(A))
