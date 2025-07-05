N,K=map(int, input().split())
S=input()
W=[]
l=1
a=S[0]
for i in range(1,N):
    if S[i]==a:
        l+=1
    else:
        W.append([a,l])
        a=S[i]
        l=1
W.append([a,l])
I=0
c=0
t=0
for j in range(len(W)):
    t+=W[j][1]
    if W[j][0]=="1":
        c+=1
    if c==K:
        I=j
        break
A=S[t:]
B=S[:t-W[I][1]-W[I-1][1]]
print(B+"1"*(W[I][1])+"0"*(W[I-1][1])+A)