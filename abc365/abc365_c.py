import collections
import bisect

n, m = map(int, input().split())
A = list(map(int, input().split()))
Al = list(set(A))
Al.sort()
Ac = collections.Counter(A)
An = [0 for i in range(len(Al))]
An[0] = n
for i in range(1, len(Al)):
    An[i] = An[i - 1] - Ac[Al[i - 1]]
Ak = [0 for i in range(len(Al))]
Ak[0] = n * Al[0]
for i in range(1, len(Al)):
    Ak[i] = Ak[i - 1] + An[i] * (Al[i] - Al[i - 1])
# print(Ak)
j = bisect.bisect(Ak, m)
if j == 0:
    print(m // n)
elif j == len(Al):
    print("infinite")
else:
    print(Al[j - 1] + (m - Ak[j - 1]) // An[j])
# print(Ak)
