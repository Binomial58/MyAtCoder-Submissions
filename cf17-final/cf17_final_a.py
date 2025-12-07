A = ["K", "I", "H", "B", "R"]
s = input()
S = []
now = 0
for i in s:
    if i != "A":
        S.append(i)
        now = 0
    else:
        now += 1
        if now == 2:
            print("NO")
            exit()
if A == S:
    if len(s) - len(S) > 5:
        print("NO")
    else:
        if "KA" in s or "IA" in s:
            print("NO")
        else:
            print("YES")
else:
    print("NO")
