import bisect

n, a, b = map(int, input().split())
s = input()
A = []
B = []
for i in range(n):
    if s[i] == "a":
        A.append(1)
        B.append(0)
    else:
        A.append(0)
        B.append(1)
for i in range(1, n):
    A[i] += A[i - 1]
    B[i] += B[i - 1]
count = 0
A = [0] + A
B = [0] + B
for l in range(1, n + 1):
    ac = bisect.bisect_left(A, A[l - 1] + a)
    bc = bisect.bisect_left(B, b + B[l - 1]) - 1
    # print(ac, bc)
    count += max(0, bc - ac + 1)
# print(A)
# print(B)
print(count)
