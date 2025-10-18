s=input()
count=0
i=0
back=""
while i<=len(s)-1:
    if s[i]==back:
        if i==len(s)-1:
            count-=1
        else:
            back=s[i]+s[i+1]
            i+=1
    else:
        back=s[i]
    i+=1
    count+=1
print(count)