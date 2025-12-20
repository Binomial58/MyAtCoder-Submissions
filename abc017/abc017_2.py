x = input()
x += "."
i = 0
while i != len(x) - 1:
    if x[i] == "o" or x[i] == "k" or x[i] == "u":
        i += 1
    elif x[i] == "c" and x[i + 1] == "h":
        i += 2
    else:
        print("NO")
        exit()
print("YES")
