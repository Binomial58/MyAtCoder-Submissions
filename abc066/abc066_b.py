s = input()
for i in range(len(s) - 1, -1, -1):
    t = s[:i]
    if len(t) % 2 == 0:
        a = t[: len(t) // 2]
        b = t[len(t) // 2 :]
        if a == b:
            print(i)
            exit()
