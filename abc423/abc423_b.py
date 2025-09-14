n=int(input())
L=list(map(int, input().split()))
r=0
l=0
for i in range(n):
    if L[i]==1:
        l=i
        break
for i in range(n-1,-1,-1):
    if L[i]==1:
        r=i
        break
print(r-l)