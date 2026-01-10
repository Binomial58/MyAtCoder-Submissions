from collections import Counter

n = int(input())
A = list(map(int, input().split()))
J = [j + 1 - A[j] for j in range(n)]
I = [i + 1 + A[i] for i in range(n)]
Jc = Counter(J)
Ic = Counter(I)
count = 0
for i in Ic:
    if i in Jc:
        count += Ic[i] * Jc[i]
print(count)
