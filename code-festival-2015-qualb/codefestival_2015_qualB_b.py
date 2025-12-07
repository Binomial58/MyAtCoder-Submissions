from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = Counter(A)
C = B.most_common()
c = C[0][1]
if c * 2 > n:
    print(C[0][0])
else:
    print("?")
