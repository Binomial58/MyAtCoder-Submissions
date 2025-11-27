import collections

n = int(input())
A = list(map(int, input().split()))
As = list(set(A))
As.sort()
Ac = collections.Counter(A)
D = dict()
for i in range(len(As)):
    D[len(As) - i - 1] = As[i]
for k in range(n):

    if k >= len(D):
        print(0)
    else:
        print(Ac[D[k]])
# print(As)
# print(Ac)
# print(D)
