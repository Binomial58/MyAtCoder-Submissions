N=int(input())
S=input()
m=0
i=0
while i<N:
    if S[i]=="/":
        j=1
        c=1
        while (i-j)!=-1 and (i+j)!=N:
            if S[i-j]=="1" and S[i+j]=="2":
                c+=2
            else:
                break
            j+=1
        m=max(m,c)
        i+=j
    i+=1
print(m)