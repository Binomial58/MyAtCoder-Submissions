D = input()
R = []
for d in D:
    if d == "N":
        R.append("S")
    elif d == "S":
        R.append("N")
    elif d == "E":
        R.append("W")
    else:
        R.append("E")
print("".join(R))
