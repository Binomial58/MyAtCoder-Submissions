S=input()
F=S
S=list(S)
L=len(S)
d=0
for i in range(L):
    D=str(S[i])
    if D.isupper():
        d+=1
if d>=(L+1)//2:
    print(F.upper())
else:
    print(F.lower())