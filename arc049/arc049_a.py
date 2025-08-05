s=input()
X=list(map(int, input().split()))
t=""
for i in range(len(s)):
    if i in X:
        t+="\""
    t+=s[i]
if len(s) in X:
    t+="\""
print(t)