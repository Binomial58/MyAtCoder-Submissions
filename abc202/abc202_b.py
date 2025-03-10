S=input()
U=[]
T=""
for i in range(len(S)):
    if S[i]=="6":
        U.append("9")
    elif S[i]=="9":
        U.append("6")
    else:
        U.append(S[i])
for k in range(len(S)-1,-1,-1):
    T+=U[k]
print(T)  