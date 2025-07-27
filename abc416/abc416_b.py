s=input()
t=""
c=0
for i in range(len(s)):
    if s[i]=="#":
        t+="#"
        c=0
    elif c==0:
        t+="o"
        c=1
    else:
        t+="."
print(t)