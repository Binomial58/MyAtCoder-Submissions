s = input()
Sn = [[0 for i in range(len(s))] for j in range(26)]
for i in range(len(s)):
    Sn[ord(s[i]) - 65][i] += 1
for i in range(26):
    for j in range(1, len(s)):
        Sn[i][j] += Sn[i][j - 1]
count = 0
for i in range(1, len(s) - 1):
    for j in range(26):
        count += Sn[j][i - 1] * (Sn[j][-1] - Sn[j][i])
print(count)
