n, t = map(str, input().split())
R = []
for i in range(int(n)):
    s = input()
    if t == s:
        R.append(i + 1)
    elif len(s) == len(t):
        count = 0
        for j in range(len(s)):
            if t[j] != s[j]:
                count += 1
        if count == 1:
            R.append(i + 1)
    elif len(s) + 1 == len(t):
        now = 0
        flag = True
        j = 0
        while j != len(s):
            if s[j] == t[j + now]:
                j += 1
            else:
                now += 1
            if now == 2:
                flag = False
                break
        if flag:
            R.append(i + 1)
    elif len(s) - 1 == len(t):
        now = 0
        flag = True
        j = 0
        while j != len(t):
            if t[j] == s[j + now]:
                j += 1
            else:
                now += 1
            if now == 2:
                flag = False
                break
        if flag:
            R.append(i + 1)
print(len(R))
print(*R)
