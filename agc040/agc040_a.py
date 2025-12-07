s = input()
l = len(s)
A = [0 for i in range(len(s) + 1)]
for i in range(1, l + 1):
    if s[i - 1] == "<":
        A[i] = A[i - 1] + 1
for i in range(l - 1, -1, -1):
    if s[i] == ">" and A[i] <= A[i + 1]:
        A[i] = A[i + 1] + 1
print(sum(A))
