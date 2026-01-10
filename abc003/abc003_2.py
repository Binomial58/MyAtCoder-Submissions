s = input()
t = input()
W = ["a", "t", "c", "o", "d", "e", "r"]
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    if s[i] != "@" and t[i] != "@":
        print("You will lose")
        exit()
    if s[i] in W or t[i] in W:
        continue
    else:
        print("You will lose")
        exit()
print("You can win")
