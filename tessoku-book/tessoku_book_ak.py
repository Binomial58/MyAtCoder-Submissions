n,m,b=map(int, input().split())
A=list(map(int, input().split()))
C=list(map(int, input().split()))
sum=0
for a in A:
    sum+=a*len(C)
for c in C:
    sum+=c*len(A)
sum+=b*len(A)*len(C)
print(sum)
