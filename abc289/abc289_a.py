s=input()
w=""
for i in range(len(s)):
    if s[i]=="0":
        w+="1"
    else:
        w+="0"
print(w)