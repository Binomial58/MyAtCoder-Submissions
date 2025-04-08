S=input()
T=0
s=0
for i in range(1,(len(S)-1)//2+1):
    for a in range(len(S)-2*i):
        if S[a]=="A" and S[a+i]=="B" and S[a+2*i]=="C":
            s+=1
print(s)