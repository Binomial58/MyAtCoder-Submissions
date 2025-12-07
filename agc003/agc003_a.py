s = input()
X = [0, 0, 0, 0]
for t in s:
    if t == "S":
        X[0] += 1
    elif t == "N":
        X[1] += 1
    elif t == "W":
        X[2] += 1
    else:
        X[3] += 1
if X[0:2].count(0) == 1 and X[2:4].count(0) == 1:
    print("No")
else:
    if X.count(0) == 1 or X.count(0) == 3:
        print("No")
    else:
        print("Yes")
