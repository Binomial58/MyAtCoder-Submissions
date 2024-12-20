N=int(input())
S=input()
T=input()
d=0
for i in range(N):
    if S[i]==T[i]:
        d+=1
    if (S[i]=="l"and T[i]=="1")or (S[i]=="1"and T[i]=="l"):
        d+=1
    if (S[i]=="o"and T[i]=="0")or (S[i]=="0"and T[i]=="o"):
        d+=1
if d==N:
    print("Yes")
else:
    print("No")