n = int(input())
T = list(map(int, input().split()))
A = [0]
for i in range(n):
    y1 = (A[i] // (2 ** (T[i])) + 1) * 2 ** (T[i])
    y2 = y1 + 2 ** (T[i])
    if y1 % (2 ** (T[i] + 1)) == 0:
        A.append(y2)
    else:
        A.append(y1)
# print(A)
print(A[-1])
