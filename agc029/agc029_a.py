s = input()
B = []
Bi = []
for i in range(len(s) - 1, -1, -1):
    if s[i] == "B":
        B.append(i)
for i in range(len(B)):
    Bi.append(len(s) - i - 1)
count = 0
for i in range(len(B)):
    count += Bi[i] - B[i]
print(count)
