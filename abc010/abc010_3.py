import math

T = list(map(int, input().split()))
t = T[4]
v = T[5]
n = int(input())
X = []
for i in range(n):
    X.append(list(map(int, input().split())))
flag = True
for i in range(n):
    x = math.sqrt((T[0] - X[i][0]) ** 2 + (T[1] - X[i][1]) ** 2) + math.sqrt(
        (X[i][0] - T[2]) ** 2 + (X[i][1] - T[3]) ** 2
    )
    # print(t, x, v)
    if t * v >= x:
        flag = False
if flag:
    print("NO")
else:
    print("YES")
