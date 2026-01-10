import itertools

A = list(map(int, input().split()))
for a in itertools.combinations(A, 5):
    a = list(a)
    a.sort()
    if len(set(a)) == 2:
        x = list(set(a))[0]
        y = list(set(a))[1]
        if (a.count(x) == 2 and a.count(y) == 3) or (
            a.count(x) == 3 and a.count(y) == 2
        ):
            print("Yes")
            exit()
print("No")
