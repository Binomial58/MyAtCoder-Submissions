n, l, r = map(int, input().split())
s = input()
for i in range(l - 1, r):
    if s[i] != "o":
        print("No")
        exit()
print("Yes")
