n, q = map(int, input().split())
s = input()
S = ["", ""]
S += [s[i] for i in range(n)]
S += ["", ""]
R = []
count = 0
for i in range(n):
    if S[i] == "A" and S[i + 1] == "B" and S[i + 2] == "C":
        count += 1
for i in range(q):
    x, c = map(str, input().split())
    x = int(x) + 1
    if S[x] == "A":
        if S[x + 1] == "B" and S[x + 2] == "C":
            count -= 1
    elif S[x] == "B":
        if S[x - 1] == "A" and S[x + 1] == "C":
            count -= 1
    elif S[x] == "C":
        if S[x - 2] == "A" and S[x - 1] == "B":
            count -= 1
    S[x] = c
    if c == "A":
        if S[x + 1] == "B" and S[x + 2] == "C":
            count += 1
    elif c == "B":
        if S[x - 1] == "A" and S[x + 1] == "C":
            count += 1
    elif c == "C":
        if S[x - 2] == "A" and S[x - 1] == "B":
            count += 1
    R.append(count)
for r in R:
    print(r)
