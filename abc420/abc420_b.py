n,m=map(int, input().split())
S=[]
M=[]
R=[]
T=[]
for i in range(n):
    s=input()
    S.append(s)
for j in range(m):
    zero=0
    one=0
    for i in range(n):
        if S[i][j]=="1":
            one+=1
        else:
            zero+=1
    if one==n or zero==n:
        M.append("2")
    else:
        if one>zero:
            M.append("0")
        else:
            M.append("1")
for j in range(n):
    c=0
    for i in range(m):
        if M[i]=="2":
            c+=1
        elif S[j][i]==M[i]:
            c+=1
    R.append(c)
maxR=max(R)
for i in range(n):
    if R[i]==maxR:
        T.append(i+1)
print(*T)