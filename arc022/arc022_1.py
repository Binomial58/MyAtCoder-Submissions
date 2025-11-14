s = input()
D = ""
for i in s:
    if i == "i" or i == "I":
        D += "I"
    elif i == "c" or i == "C":
        D += "C"
    elif i == "t" or i == "T":
        D += "T"
E = ""
for d in D:
    if E == "" and d == "I":
        E += d
    elif E == "I" and d == "C":
        E += d
    elif E == "IC" and d == "T":
        E += d
if E == "ICT":
    print("YES")
else:
    print("NO")
