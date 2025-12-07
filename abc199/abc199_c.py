n = int(input())
s = input()
S = [s[i] for i in range(2 * n)]
q = int(input())
# 文字列が反転しているかの管理
rev = False
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if rev:
            if a >= n:
                a -= n
            else:
                a += n
            if b >= n:
                b -= n
            else:
                b += n
        S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
    else:
        rev = not rev
if rev:
    print("".join(S[n:] + S[:n]))
else:
    print("".join(S))
