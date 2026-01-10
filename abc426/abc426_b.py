s = list(input())
S = set(s)
for t in S:
    if s.count(t) == 1:
        print(t)
        exit()
