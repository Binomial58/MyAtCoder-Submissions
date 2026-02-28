from collections import Counter

s = input()
C = Counter(s)
maxi = 0
for t in s:
    maxi = max(maxi, C[t])
ans = ""
count = 0
for t in s:
    if C[t] != maxi:
        ans += t
        count += 1
if count == 0:
    print("")
else:
    print(ans)
