N=int(input())
S=[]
d=0
e=0
k=0
for i in range(N):
    S.append(input())
while d!=2 and e!=N:
    if S[k]=="sweet":
        d+=1
    else:
        d=0
    e+=1
    k+=1
if e==N:
    print("Yes")
else:
    print("No")