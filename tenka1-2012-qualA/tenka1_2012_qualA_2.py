c = input()


W = []
l = 1
a = c[0]
for i in range(1, len(c)):
    if c[i] == a:
        l += 1
    else:
        W.append([a, l])
        a = c[i]
        l = 1
W.append([a, l])
S = []
for w in W:
    if w[0] != " ":
        for i in range(w[1]):
            S.append(w[0])
    else:
        S.append(",")
print("".join(S))
