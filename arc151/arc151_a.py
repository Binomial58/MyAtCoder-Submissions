n = int(input())
s = input()
t = input()
# sとtのハミング距離
hd = 0
# 同じ文字のインデックス
A = set()
for i in range(n):
    if s[i] != t[i]:
        hd += 1
    else:
        A.add(i)
if hd % 2 == 1:
    print("-1")
else:
    H = [s, t]
    hd //= 2
    H.sort()
    s = H[0]
    t = H[1]
    R = []
    sh = 0
    th = 0
    for i in range(n):
        if i in A:
            R.append("0")
        else:
            if s[i] == "0":
                if sh != hd:
                    R.append(s[i])
                    sh += 1
                else:
                    R.append(t[i])
                    th += 1
            else:
                if th != hd:
                    R.append(t[i])
                    th += 1
                else:
                    R.append(s[i])
                    sh += 1
    print("".join(R))
