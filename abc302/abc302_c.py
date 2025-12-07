import itertools

n, m = map(int, input().split())
S = [input() for i in range(n)]
for s in itertools.permutations(S):
    flag = True
    for i in range(n - 1):
        a = s[i]
        b = s[i + 1]
        count = m
        for j in range(m):
            if a[j] == b[j]:
                count -= 1
        if count != 1:
            flag = False
    if flag:
        print("Yes")
        exit()
print("No")
