N=int(input())
S=input()
R=""
W=[]
V=[]
r=S[0]
c=1
for i in range(1,N):
    if S[i]==r:
        c+=1
    else:
        W.append(c)
        c=1
        r=S[i]
if r=="1":
    W.append(c)
r="1"
V.append(W[0])
for i in range(1,len(W)):
    V.append(V[i-1]+W[i])
V=V[::-1]
for i in range(len(W)):
    if r=="1":
        R+="A"*(V[i])
        r="0"
    else:
        R+="B"*(V[i])
        r="1" 
print(len(R))
print(R)