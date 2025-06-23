N=int(input())
S={}
U=[]
for i in range(N):
    s=input()
    if s in S:
        I=S[s]+1
        S[s]=I
        U.append(s+"("+str(S[s])+")")
    else:
        S[s]=0
        U.append(s)
for u in U:
    print(u)