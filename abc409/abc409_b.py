N=int(input())
A=list(map(int, input().split()))
m=N
for i in range(N+1):
    s=0
    for j in range(N):
        if A[j]>=i:
            s+=1
    if s>=i:
        m=i
print(m)