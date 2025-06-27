s=input()
L=len(s)//2
for i in range(L):
    if s[i]!=s[len(s)-1-i]:
        if s[i]!="*" and s[len(s)-1-i]!="*":
            print("NO")
            exit()
print("YES")