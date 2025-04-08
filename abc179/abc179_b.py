N=int(input())
C=0
D=0
for _ in range(N):
    a,b=map(int, input().split())
    if a==b:
        C+=1
    else:
        C=0
    if C==3:
        D+=1
if D==0:
    print("No")
else:
    print("Yes")