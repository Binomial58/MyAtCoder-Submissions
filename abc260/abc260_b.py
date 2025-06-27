N,X,Y,Z=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=[]
for i in range(N):
    C.append(A[i]+B[i])
a=[i for i in range(1,N+1)]
b=[i for i in range(1,N+1)]
c=[i for i in range(1,N+1)]
I=[]
L=[]
math=[[A[i],a[i]]for i in range(N)]
math=sorted(math,key=lambda x:(-x[0],x[1]))
Eng=[[B[i],b[i]]for i in range(N)]
Eng=sorted(Eng,key=lambda x:(-x[0],x[1]))
SUM=[[C[i],c[i]]for i in range(N)]
SUM=sorted(SUM,key=lambda x:(-x[0],x[1]))
for i in range(X):
    I.append(math[i][0])
    L.append(math[i][1])
j=0
c=0
while j!=Y:
    if Eng[j+c][1]in L:
        c+=1
    else:
        I.append(Eng[j+c][0])
        L.append(Eng[j+c][1])
        j+=1
j=0
c=0
while j!=Z:
    if SUM[j+c][1]in L:
        c+=1
    else:
        I.append(SUM[j+c][0])
        L.append(SUM[j+c][1])
        j+=1
L.sort()
for l in L:
    print(l)


