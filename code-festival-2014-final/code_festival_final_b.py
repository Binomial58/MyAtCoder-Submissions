s=input()
c=0
for i in range(1,len(s)+1):
    if i%2==1:
        c+=int(s[i-1])
    else:
        c-=int(s[i-1])
print(c)