n = int(input())
R = set()
for i in range(10000):
    s = str(n)
    count = 0
    for i in range(len(s)):
        count += int(s[i]) ** 2
    n = count
    R.add(n)
if 1 in R:
    print("Yes")
else:
    print("No")
