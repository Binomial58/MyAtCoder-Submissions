n=int(input())
A=list(map(int, input().split()))
B={}
R=[]
for i in range(n):
    B[A[i]]=i+1
j=-1
for i in range(n):
    R.append(B[j])
    j=B[j]
print(*R)