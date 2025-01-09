S=input()
k=0
count=0
if S=="0":
    print(1)
    exit()
while k<len(S)-1:
    if S[k]=="0" and S[k+1]=="0":
        k+=1
        count+=1
    k+=1
print(len(S)-count)