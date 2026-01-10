n = int(input())
S = input()
A = [i * 2 for i in range(n)]
B = [1 + i * 2 for i in range(n)]
I = []
for i in range(2 * n):
    if S[i] == "A":
        I.append(i)
a = 0
b = 0
for i in range(n):
    a += abs(A[i] - I[i])
    b += abs(B[i] - I[i])
print(min(a, b))
