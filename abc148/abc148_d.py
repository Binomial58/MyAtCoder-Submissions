N=int(input())
A=list(map(int, input().split()))
c=0
j=1
for i in range(N):
    if A[i]!=j:
        c+=1
    else:
        j+=1
if c==N:
    print(-1)
else:
    print(c)