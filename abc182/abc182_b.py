N=int(input())
A=list(map(int, input().split()))
M=1
c=2
for i in range(2,max(A)+1):
    k=0
    for a in A:
        if a%i==0:
            k+=1
    if k>=M:
        c=i
        M=k
print(c)