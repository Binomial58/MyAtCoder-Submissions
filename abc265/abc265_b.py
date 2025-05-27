N,M,T=map(int, input().split())
A=list(map(int, input().split()))
X=set()
Y=[]
j=0
for  i in range(M):
    x,y=map(int, input().split())
    X.add(x)
    Y.append(y)
for i in range(N-1):
    T-=A[i]
    if T<=0:
        print("No")
        exit()
    if i+2 in X:
        T+=Y[j]
        j+=1
print("Yes")