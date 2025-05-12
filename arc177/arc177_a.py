M=list(map(int, input().split()))
K=[1,5,10,50,100,500]
N=int(input())
X=list(map(int, input().split()))
for i in range(N):
    for j in range(5,-1,-1):
        if X[i]>=K[j] and M[j]>0:
            a=X[i]//K[j]
            if M[j]>=a:
                X[i]-=a*K[j]
                M[j]-=a
            else:
                X[i]-=M[j]*K[j]
                M[j]-=M[j]
for x in X:
    if x!=0:
        print("No")
        exit()
print("Yes")
