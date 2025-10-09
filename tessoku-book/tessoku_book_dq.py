n=int(input())
A=[]
R=[]
now=[i for i in range(n)]
for i in range(n):
    A.append(list(map(int, input().split())))
q=int(input())
for i in range(q):
    Q=list(map(int, input().split()))
    if Q[0]==1:
        a=now[Q[2]-1]
        b=now[Q[1]-1]
        now[Q[1]-1]=a
        now[Q[2]-1]=b
    else:
        R.append(A[now[Q[1]-1]][Q[2]-1])
for r in R:
    print(r)