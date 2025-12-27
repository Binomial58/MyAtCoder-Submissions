import itertools

n, k = map(int, input().split())
S = list(input())
T = set()
for s in itertools.permutations(S):
    T.add(s)
count = len(T)
if len(S) == len(set(S)):
    print(count)
else:
    for t in T:
        # print(t)
        x = t
        y = t[::-1]
        # print(t)
        for i in range(n - k + 1):
            # print(t[i : i + k], t[i : i + k][::-1])
            if t[i : i + k] == t[i : i + k][::-1]:
                count -= 1
                break
            # print(t[i : i + k][::-1])
    print(count)
