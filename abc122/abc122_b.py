S=input()
C=0
M=0
for i in range(len(S)):
    if S[i]=="A" or S[i]=="C" or S[i]=="G" or S[i]=="T":
        C+=1
        M=max(M,C)
    else:
        C=0
print(M)