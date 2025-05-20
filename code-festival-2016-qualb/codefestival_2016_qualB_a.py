S=input()
T="CODEFESTIVAL2016"
C=0
for i in range(len(S)):
    if S[i]!=T[i]:
        C+=1
print(C)