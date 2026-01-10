x = int(input())
n = int(input())
W = list(map(int, input().split()))
q = int(input())
R = []
Now = [0 for i in range(n)]
for i in range(q):
    p = int(input())
    if Now[p - 1] == 0:
        Now[p - 1] = W[p - 1]
    else:
        Now[p - 1] = 0
    R.append(x + sum(Now))
for r in R:
    print(r)
