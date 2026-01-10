n = int(input())
R = []
i = 1
while i * i <= n:
    R.append(i * i)
    i += 1
D = dict()
for i in range(len(R)):
    for j in range(len(R)):
        if i > j:
            if R[i] + R[j] in D:
                D[R[i] + R[j]] += 1
            elif R[i] + R[j] <= n:
                D[R[i] + R[j]] = 1
Ans = []
for d in D:
    if D[d] == 1:
        Ans.append(d)
print(len(Ans))
Ans.sort()
print(*Ans)
# print(len(R))
# print(D)
