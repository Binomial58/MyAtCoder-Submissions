N=int(input())
A=list(map(int, input().split()))
C=0
D=0
for a in A:
    if a%2==0:     
        C+=1
        if a%3==0 or a%5==0:
            D+=1
if C==D:
    print("APPROVED")
else:
    print("DENIED")