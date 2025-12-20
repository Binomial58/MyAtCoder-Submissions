from collections import Counter

n = int(input())
A = list(map(int, input().split()))
B = Counter(A)
As = sum(A)
R = []
# print(B)
q = int(input())
for i in range(q):
    b, c = map(int, input().split())
    As -= b * B[b]
    As += c * B[b]
    d = B[b]
    if b in B:
        B.pop(b)
    if c in B:
        B[c] += d
    else:
        B[c] = d
    R.append(As)
    # print(B)
for r in R:
    print(r)