s = input()
C = dict()
for t in s:
    if t not in C:
        C[t] = 1
    else:
        C[t] += 1
count = 0
for j in range(len(s)):
    count += (len(s)) - C[s[j]]
if len(s) == len(C):
    print(count // 2)
else:
    print(count // 2 + 1)
