n = int(input())
S = [input() for i in range(n)]
C = [0 for i in range(n)]
for i in range(n):
    for j in range(n):
        if S[i][j] == "o":
            C[j] += 1
# print(C)
count = 0
for i in range(n):
    c = S[i].count("o")
    if c >= 2:
        for j in range(n):
            if S[i][j] == "o":
                count += (C[j] - 1) * (c - 1)
print(count)
