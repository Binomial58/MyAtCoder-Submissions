from collections import Counter

n = int(input())
S = []
for i in range(n):
    S.append(input())
C = Counter(S)
d = C.most_common()
print(d[0][0])
