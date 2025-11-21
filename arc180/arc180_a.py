n = int(input())
s = input()
S = []
for i in range(n):
    if (i + 1) % 2 == 0:
        if s[i] == "A":
            S.append("B")
        else:
            S.append("A")
    else:
        S.append(s[i])
t = "".join(S)
W = []
l = 1
a = t[0]
for i in range(1, n):
    if S[i] == a:
        l += 1
    else:
        W.append(l)
        a = S[i]
        l = 1
W.append(l)
count = 1
for w in W:
    count *= (w + 1) // 2
    count %= 10**9 + 7
print(count)
