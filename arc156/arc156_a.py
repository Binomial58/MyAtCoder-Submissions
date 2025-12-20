t = int(input())
R = []
for k in range(t):
    n = int(input())
    s = input()
    c = s.count("1")
    if c % 2 == 1:
        R.append(-1)
    elif c != 2:
        R.append(c // 2)
    else:
        now = 0
        i = 0
        while now != c // 2:
            if s[i] == "1":
                now += 1
                break
            i += 1
        if s[i + 1] == "1":
            if n == 3:
                R.append(-1)
            elif n == 4:
                if i == 0 or i == 2:
                    R.append(c // 2 + 1)
                else:
                    R.append(c // 2 + 2)
            else:
                R.append(c // 2 + 1)
        else:
            R.append(c // 2)
for r in R:
    print(r)
