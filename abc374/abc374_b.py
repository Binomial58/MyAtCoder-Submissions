S=list(input())
T=list(input())
L_S=len(S)
L_T=len(T)
if L_S>L_T:
    A=L_S-L_T
    for i in range(A):
        T.append("0")
        L=L_S
elif L_S<L_T:
    A=L_T-L_S
    for i in range(A):
        S.append("0")
        L=L_T
else:
    L=L_S
for i in range(L):
    if S[i]!=T[i]:
        print(i+1)
        break
if all(S[k]==T[k] for k in range(L)):
    print(0)