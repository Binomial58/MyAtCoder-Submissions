n,q=map(int, input().split())
A=list(map(int, input().split()))
A+=A
sumA=[0]
a=0
R=[]
for i in range(2*n):
    sumA.append(sumA[i]+A[i])
for i in range(q):
    Q=list(map(str, input().split()))
    if Q[0]=="1":
        c=int(Q[1])
        a+=c
        if a>=n:
            a=a%n
    else:
        l=int(Q[1])
        r=int(Q[2])
        R.append(sumA[a+r]-sumA[a+l-1])
for r in R:
    print(r)