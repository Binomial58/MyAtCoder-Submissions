s = input()
T = []
flag = True
for i in range(len(s)):
    if s[i] == "#":
        T.append("#")
        flag = True
    elif flag:
        T.append("o")
        flag = False
    else:
        T.append(".")
print("".join(T))
