n = int(input())
t = input()
s = "110" * n
id = -1
for i in range(3):
    if t == s[i : i + n]:
        id = i
if id == -1:
    print(0)
else:
    if t == "1":
        print(10**10 * 2)
    else:
        l = (id + n + 2) // 3
        print(10**10 - l + 1)
