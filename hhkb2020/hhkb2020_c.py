N = int(input())
P = list(map(int, input().split()))
# 現状の答え
x = 0
# iの時の集合
PX = set()
for p in P:
    PX.add(p)
    while x in PX:
        x += 1
    print(x)
