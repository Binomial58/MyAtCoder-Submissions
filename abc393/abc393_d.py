n = int(input())
s = input()
count = 0
now = 0
for i in range(n):
    if s[i] == "1":
        now += 1
    else:
        count += min(now, s.count("1") - now)
print(count)
