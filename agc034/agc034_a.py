n, a, b, c, d = map(int, input().split())
s = input()
A = [False] * n
B = [False] * n
A[a - 1] = True
B[b - 1] = True
for i in range(n - 2):
    if A[i]:
        if s[i + 1] == ".":
            A[i + 1] = True
        if s[i + 2] == ".":
            A[i + 2] = True
    if B[i]:
        if s[i + 1] == ".":
            B[i + 1] = True
        if s[i + 2] == ".":
            B[i + 2] = True
if s[-1] == ".":
    if A[n - 2]:
        A[-1] = True
    if B[n - 2]:
        B[-1] = True
if c < d:
    if A[c - 1] and B[d - 1]:
        print("Yes")
    else:
        print("No")
else:
    if "..." in s[b - 2 : d + 1]:
        print("Yes")
    else:
        print("No")
#     print(s[b - 1 : d + 1])

# print(A)
# print(B)
