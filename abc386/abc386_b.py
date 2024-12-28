S=input()
c=0
k=0
while k !=(len(S)):
    if k!=len(S)-1 and S[k]=="0" and S[k+1]=="0":
        k+=1
    c+=1
    k+=1
print(c)