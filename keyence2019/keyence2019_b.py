s = input()
A = ["k", "e", "y", "e", "n", "c", "e", ""]
if s == "keyence":
    print("YES")
else:
    i = 0
    for t in s:
        if t == A[i]:
            i += 1
        else:
            break
    u = s[:i] + s[len(s) - 7 + i :]
    if u == "keyence":
        print("YES")
    else:
        print("NO")
