N,M=map(int,input().split())
A=[]
B=[]
C=[0]*N
for i in range(M):
    a,b=input().split()
    a=int(a)
    A.append(a)
    B.append(b)
for k in range(M):
    if B[k]=="F":
        print("No")
    else:
        C[A[k]-1]+=1
        if C[A[k]-1]==1:
            print("Yes")
        else:
            print("No")