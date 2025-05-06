S=input()
T=input()
C=0
D=0
if S==T:
    print("Yes")
    exit()
for i in range(len(S)-1):
    if S[i]!=T[i] and S[i+1]!=T[i+1] and S[i]==T[i+1] and S[i+1]==T[i]:
        C+=1
for j in range(len(S)):
    if S[j]!=T[j]:
        D+=1
if C==1 and D==2:
    print("Yes")
else:
    print("No")