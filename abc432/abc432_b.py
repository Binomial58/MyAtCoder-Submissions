x = input()
X = []
for i in x:
    if i != "0":
        X.append(int(i))
count = x.count("0")
X.sort()
t = str(X[0])
t += "0" * count
for i in range(1, len(X)):
    t += str(X[i])
print(int(t))
