S=input()
L=len(S)
I=[0]*(L)
for k in range(L):
    for j in range(k+1):
        if S[k]==S[j]:
            I[j]+=1
            break
Max=max(I)
for i in range(1,Max+1):
    if I.count(i)!=0 and I.count(i)!=2:
        print("No")
        exit()
print("Yes")