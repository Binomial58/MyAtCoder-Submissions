N=int(input())
A=list(map(int, input().split()))
K=int(input())
c=0
for a in A:
    if K<=a:
        c+=1
print(c)