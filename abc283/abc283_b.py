N=int(input())
A=list(map(int, input().split()))
Q=int(input())
B=[]
for _ in range(Q): 
    q=list(map(int, input().split()))
    if q[0]==1:
        A[q[1]-1]=q[2]
    else:
        B.append(A[q[1]-1]) 
for b in B:
    print(b)