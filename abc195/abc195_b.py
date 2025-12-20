a, b, w = map(int, input().split())
w *= 1000
maxo = -1
mino = 10**10
flag = False
for i in range(1, w + 1):
    c = w / i
    if a <= c <= b:
        maxo = max(maxo, i)
        mino = min(mino, i)
        flag = True
if flag:
    print(mino, maxo)
else:
    print("UNSATISFIABLE")