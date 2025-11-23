s = input()
X = [int(s[i]) for i in range(4)]
O = ["+", "-"]
for a in range(2):
    for b in range(2):
        for c in range(2):
            now = X[0]
            if a == 0:
                now += X[1]
            else:
                now -= X[1]
            if b == 0:
                now += X[2]
            else:
                now -= X[2]
            if c == 0:
                now += X[3]
            else:
                now -= X[3]
            if now == 7:
                print(
                    str(X[0])
                    + O[a]
                    + str(X[1])
                    + O[b]
                    + str(X[2])
                    + O[c]
                    + str(X[3])
                    + "=7"
                )
                exit()
