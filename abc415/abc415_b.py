s = input()
R = []
for i in range(len(s)):
    if s[i] == "#":
        R.append(i + 1)
for i in range(len(R) // 2):
    print(str(R[i * 2]) + "," + str(R[1 + i * 2]))
