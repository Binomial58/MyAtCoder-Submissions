A=list(map(int, input().split()))
if (A[0]+A[2])%2==1:
    A[2]+=1
    c=1
else:
    c=0
if A[0]+A[2]<A[1]*2:
    print(A[1]*2-A[0]-A[2]+c)
else:
    print((A[0]+A[2]-2*A[1])//2+c)