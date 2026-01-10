n = int(input())
I = ["M", "A", "R", "C", "H"]
N = [0 for i in range(5)]
for i in range(n):
    s = input()
    if s[0] in I:
        N[I.index(s[0])] += 1
# print(N)
count = 0
for i in range(1 << 5):
    B = []
    for j in range(5):
        if (i >> j) & 1:
            B.append(j)
    if len(B) == 3:
        count += N[B[0]] * N[B[1]] * N[B[2]]
print(count)
