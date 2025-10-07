x,y=map(int, input().split())
a,b=max(x,y),min(x,y)
R=[]
W=[[],[]]
r=-1
while r!=0:
    q=a//b
    r=a%b
    R.append([a,b,q])
    a=b
    b=r
if R[0][0]==x:
    s=0
else:
    s=1
for A in R:
    if s==0:
        W[0].append(A[0])
        W[1].append(A[1])
        s=1
        for i in range(A[2]-1):
            W[0].append(W[0][-1]-A[1])
            W[1].append(A[1])
    else:
        W[1].append(A[0])
        W[0].append(A[1])
        s=0
        for i in range(A[2]-1):
            W[0].append(A[1])
            W[1].append(W[1][-1]-A[1])
W[0]=W[0][::-1][1:]
W[1]=W[1][::-1][1:]
print(len(W[0]))
for i in range(len(W[1])):
    print(W[0][i],W[1][i])