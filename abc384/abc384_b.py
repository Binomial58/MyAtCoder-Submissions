N,R=map(int, input().split())
A=[]
for _ in range(N):
    A.append(list(map(int, input().split())))
for k in range(N):
    if A[k][0]==1 and 1600<=R<=2799:
        R+=A[k][1]
    elif A[k][0]==2 and 1200<=R<=2399:
        R+=A[k][1]
print(R)