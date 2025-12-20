s = input()
t = "WBWBWWBWBWBW"
t *= 3
# print(t)
B = ["Do", "Re", "Mi", "Fa", "So", "La", "Si"]
count = 0
i = 0
while s != t[i : i + 20]:
    if t[i] == "W":
        count += 1
    i += 1
print(B[count])