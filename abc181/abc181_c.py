def inc(A,B):
    if A[0]==B[0]:
        return 10**10
    else:
        return (A[1]-B[1])/(A[0]-B[0])
        
n=int(input())
P=[]
for i in range(n):
    P.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        for k in range(n):
            if j==k or i==k:
                continue
            if inc(P[i],P[j])==inc(P[j],P[k]):
                print("Yes")
                exit()
print("No")