x = int(input())
n = int(input())
W = list(map(int, input().split()))
q = int(input())
Now = [False for i in range(n)]
R = []
for i in range(q):
    p = int(input()) - 1
    if Now[p]:
        Now[p] = not Now[p]
        x -= W[p]
    else:
        Now[p] = not Now[p]
        x += W[p]
    R.append(x)
for r in R:
    print(r)
