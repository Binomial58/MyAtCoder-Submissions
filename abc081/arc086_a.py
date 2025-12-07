from collections import Counter

n, k = map(int, input().split())
A = list(map(int, input().split()))
C = Counter(A)
D = C.most_common()
count = 0
for i in range(len(D) - k):
    count += D[len(D) - i - 1][1]
print(count)
