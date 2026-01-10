s = input()
R = []
now = 0
for i in range(1, len(s) + 1):
    if (i + now) % 2 == 1 and s[i - 1] == "o":
        now += 1
    elif (i + now) % 2 == 0 and s[i - 1] == "i":
        now += 1
if (len(s) + now) % 2 == 0:
    print(now)
else:
    print(now + 1)
