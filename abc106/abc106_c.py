s = input()
k = int(input())
j = 0
for i in range(len(s)):
    if s[i] == "1":
        j += 1
    else:
        break
if k > j:
    print(int(s[j]))
else:
    print(1)
