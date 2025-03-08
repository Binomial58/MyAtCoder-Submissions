N=int(input())
A=list(map(int, input().split()))
c=0
for i in range(N-1):
    if A[i]==A[i+1]:
        c+=1
    else:
        c=0
    if c==2:
        print("Yes")
        exit()
print("No")